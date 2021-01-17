import unittest
from delayed_assert import delayed_assert, expect, assert_expectations

class ExampleUnittest(unittest.TestCase):

    def testSomething(self):
        delayed_assert.expect(1 == 1) # will succeed
        delayed_assert.expect(1 == 2) # will fail but won't stop execution
        delayed_assert.expect(3 == 2, "Value don't match") # will fail but won't stop execution
        delayed_assert.expect(3 == 3) # will succeed
        # will stop execution and show the stack trace of 2nd assertion
        delayed_assert.assert_expectations()

    def testLambdas(self):
        expect(lambda: self.assertEqual(3,4)) # will fail but won't stop execution
        expect(lambda: self.assertListEqual([4,5,6,2,5],[7,8])) # will fail but won't stop execution
        assert_expectations()

    @delayed_assert.assert_all()
    def testDecorator(self):
        expect('five' == 'Six', 'String do not match')
        expect([5,2] == [3,4], 'List item do not match')
        expect([3,4] == [3,4], 'This message wont be printed')
        # No need to call delayed_assert.assert_expectations() when decorator is used
    
    def testContextManeger(self):
        with delayed_assert.assert_all():
            expect('four' == 'Six', 'String do not match')
            expect([5,2] == [3,4], 'List item do not match')
            expect([3,4] == [3,4], 'This message wont be printed')
            # No need to call delayed_assert.assert_expectations() when using context maneger is used

    @delayed_assert.assert_all()
    def testMethodChainCall(self):
        self.verify()
        expect('No' == 'yes', 'Printed after Distributed expect method call')

    def verify(self):
        expect(not False, 'Distributed expect method call')