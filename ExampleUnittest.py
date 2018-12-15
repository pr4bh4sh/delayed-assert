import unittest
from delayed_assert import delayed_assert

class ExampleUnittest(unittest.TestCase):

    def testSomething(self):
        delayed_assert.expect(1 == 1) # will succeed

        delayed_assert.expect(1 == 2) # will fail but won't stop execution

        delayed_assert.expect(3 == 2, "Value don't match") # will fail but won't stop execution

        delayed_assert.expect(3 == 3) # will succeed
        
        # will stop execution and show the stack trace of 2nd assertion
        delayed_assert.assert_expectations()
