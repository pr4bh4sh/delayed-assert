import unittest
from delayed_assert import delayed_assert


class PythonVersionCompatibilityTest(unittest.TestCase):

    @staticmethod
    def test():
        try:
            delayed_assert.expect(1 == 2)  # will fail but won't stop execution
            delayed_assert.assert_expectations()
        except AssertionError as e:
            pass
