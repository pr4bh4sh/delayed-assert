"""
Implements one form of delayed assertions.

Interface is 2 functions:

  expect(expr, msg=None)
  : Evaluate 'expr' as a boolean, and keeps track of failures

  assert_expectations()
  : raises an assert if an expect() calls failed

Usage Example:

    from delayed_assert import expect, assert_expectations

    def test_should_pass():
        expect(1 == 1, 'one is one')
        assert_expectations()

    def test_should_fail():
        expect(1 == 2, 'one is two')
        expect(1 == 3, 'one is three')
        assert_expectations()

https://github.com/rackerlabs/python-proboscis/blob/master/proboscis/check.py

"""

import types
import inspect
import os
from contextlib import contextmanager


# Global flag to control colorization
# Can be controlled via environment variable DELAYED_ASSERT_ENABLE_COLOR
# or programmatically via set_color_enabled()
_color_enabled = os.environ.get('DELAYED_ASSERT_ENABLE_COLOR', '1').lower() not in ('0', 'false', 'no', 'off')


class Color:
    """Colors definition with ANSI escape codes."""

    HEADER = '\033[35m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\33[5m'


class NoColor:
    """No-color definition - all attributes return empty strings."""

    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''
    BLINK = ''


def _get_color_instance():
    """Get the appropriate color instance based on the enabled flag."""
    return Color if _color_enabled else NoColor


def set_color_enabled(enabled):
    """
    Enable or disable color output.
    
    Args:
        enabled (bool): True to enable colors, False to disable
    """
    global _color_enabled
    _color_enabled = enabled


def get_color_enabled():
    """
    Get the current color enabled status.
    
    Returns:
        bool: True if colors are enabled, False otherwise
    """
    return _color_enabled


# Global flag to control caller verification
# Can be controlled via environment variable DELAYED_ASSERT_CHECK_CALLER
# or programmatically via set_check_caller()
_check_caller = os.environ.get('DELAYED_ASSERT_CHECK_CALLER', '1').lower() not in ('0', 'false', 'no', 'off')


def set_check_caller(enabled):
    """
    Enable or disable caller verification.
    
    Args:
        enabled (bool): True to enable caller verification, False to disable
    """
    global _check_caller
    _check_caller = enabled


def get_check_caller():
    """
    Get the current caller verification status.
    
    Returns:
        bool: True if caller verification is enabled, False otherwise
    """
    return _check_caller


_failed_expectations = []
_is_first_call = dict()


def _log_failure(msg=None):
    """Collect failure log."""
    color = _get_color_instance()
    file_path, line, funcname, contextlist = inspect.stack()[2][1:5]
    context = contextlist[0]
    _failed_expectations.append(
        color.FAIL+'Failed at "' + color.ENDC + color.OKBLUE + color.UNDERLINE
        + '%s:%s' % (file_path, line) + color.ENDC + color.FAIL +
        '", in %s()%s\n%s' % (
            funcname,
            ('\n\t' + color.BOLD + color.UNDERLINE + 'ErrorMessage:' +
             color.ENDC + color.FAIL + '\t%s' % msg + color.ENDC),
            context)
    )


def _report_failures():
    """Report collected failures."""
    global _failed_expectations
    color = _get_color_instance()
    report = []

    if _failed_expectations:
        file_path, line, funcname = inspect.stack()[2][1:4]
        report = [
            color.WARNING + '\n\nassert_expectations() called at' + color.ENDC,
            color.UNDERLINE + color.OKBLUE + '"%s:%s"' % (file_path, line) +
            color.ENDC + color.WARNING + ' in %s()\n' % funcname,
            color.FAIL + color.UNDERLINE + 'Failed Expectations : %s\n' %
            len(_failed_expectations) + color.ENDC]
        for i, failure in enumerate(_failed_expectations, start=1):
            report.append('%d: %s' % (i, failure))
        _failed_expectations = []

    return '\n'.join(report)


def expect(expr, msg=None):
    """Keep track of failed expectations."""
    global _failed_expectations, _is_first_call  # noqa: F824
    caller = ''

    # Ensure that the call is coming from 'test*' method
    stack_list = inspect.stack()
    for stack in stack_list:
        func_name = getattr(stack, 'function', stack[3])
        if func_name.__contains__('test'):
            caller = func_name
            break

    if caller == '':
        if _check_caller:
            raise Exception(
                'Could not identify test method, make sure the call for "expect" '
                'method is originated with "test" method')

    if _is_first_call.get(caller, True):
        _failed_expectations = []
        _is_first_call[caller] = False

    # Python lambda does not support statement inside lambda, so
    # `lambda: assert 1 == 1` won't work as it's not valid lambda expression
    if isinstance(expr, types.FunctionType):
        try:
            expr()
        except Exception as exc:
            _log_failure(exc)
    elif not expr:
        _log_failure(msg)


def assert_expectations():
    """Raise an assert if there are any failed expectations."""
    if _failed_expectations:
        assert False, _report_failures()


@contextmanager
def assert_all():
    """Context manager."""
    try:
        yield
    finally:
        assert_expectations()
