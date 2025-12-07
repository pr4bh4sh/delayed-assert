import unittest
from delayed_assert import delayed_assert, expect, assert_expectations


class PythonVersionCompatibilityTest(unittest.TestCase):

    @staticmethod
    def test():
        try:
            delayed_assert.expect(1 == 2)  # will fail but won't stop execution
            delayed_assert.assert_expectations()
        except AssertionError as e:
            pass


class TestExpectationReset(unittest.TestCase):
    """Test that expectations are properly reset between test methods."""
    
    def test_first_method_with_failure(self):
        """First test method with a failure."""
        expect(1 == 2, "First test failure")
        
        try:
            assert_expectations()
            self.fail("Should have raised AssertionError")
        except AssertionError as e:
            output = str(e)
            self.assertIn('Failed Expectations : 1', output)
            self.assertIn('First test failure', output)
    
    def test_second_method_with_failure(self):
        """Second test method - should not accumulate failures from first test."""
        expect(2 == 3, "Second test failure")
        
        try:
            assert_expectations()
            self.fail("Should have raised AssertionError")
        except AssertionError as e:
            output = str(e)
            # Should only have 1 failure, not 2 (proving _is_first_call works)
            self.assertIn('Failed Expectations : 1', output)
            self.assertIn('Second test failure', output)
            self.assertNotIn('First test failure', output)
