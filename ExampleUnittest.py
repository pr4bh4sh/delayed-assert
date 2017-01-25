import unittest
from delayed_assert import delayed_assert

class ExampleUnittest(unittest.TestCase):

    def testSomething(self):
        # will succeed
        delayed_assert.expect(1 == 1)
        # will fail
        delayed_assert.expect(1 == 2)
        delayed_assert.assert_expectations()
