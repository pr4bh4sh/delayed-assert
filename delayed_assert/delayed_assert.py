'''
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
'''

# ---------------------------------------------------

def expect(expr, msg=None):
    'keeps track of failed expectations'
    global _failed_expectations, _is_first_call
    
    caller = inspect.stack()[1][3]    
    if _is_first_call.get(caller, True):
        _failed_expectations = []
        _is_first_call[caller] = False

    if not expr:
        _log_failure(msg)

def assert_expectations():
    'raise an assert if there are any failed expectations'
    if _failed_expectations:
        assert False, _report_failures()

# ---------------------------------------------------

import inspect
import os.path

_failed_expectations = []
_is_first_call = dict()

def _log_failure(msg=None):
    (file_path, line, funcname, contextlist) =  inspect.stack()[2][1:5]
    context = contextlist[0]
    _failed_expectations.append(Color.FAIL+'Failed at "'+ Color.ENDC + Color.OKBLUE + Color.UNDERLINE + '%s:%s' % (file_path, line) + Color.ENDC + Color.FAIL + '", in %s()%s\n%s' %
        (funcname, ((Color.BOLD + Color.UNDERLINE + '\nErrorMessage: %s' % msg) + Color.ENDC if msg else ''+Color.ENDC), context))

def _report_failures():
    global _failed_expectations
    if _failed_expectations:
        (file_path, line, funcname) =  inspect.stack()[2][1:4]
        report = [
            Color.WARNING + '\n\nassert_expectations() called at' + Color.ENDC,
            Color.UNDERLINE + Color.OKBLUE+'"%s:%s"' % (file_path, line) + Color.ENDC + Color.WARNING +' in %s()\n' % (funcname),
            Color.FAIL + Color.UNDERLINE + 'Failed Expectations : %s\n' % len(_failed_expectations) + Color.ENDC]
        for i,failure in enumerate(_failed_expectations, start=1):
            report.append('%d: %s' % (i, failure))
        _failed_expectations = []
    return ('\n'.join(report))
 

class Color:
    HEADER = '\033[35m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\33[5m'
