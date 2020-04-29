[![Build Status](https://travis-ci.org/pr4bh4sh/delayed-assert.svg?branch=master)](https://travis-ci.org/pr4bh4sh/delayed-assert)
[![PyPI version](https://badge.fury.io/py/delayed-assert.svg)](https://badge.fury.io/py/delayed-assert)
[![Downloads](https://pepy.tech/badge/delayed-assert)](https://pepy.tech/project/delayed-assert)
[![Downloads](https://pepy.tech/badge/delayed-assert/month)](https://pepy.tech/project/delayed-assert)

# Python-Delayed-Assert

Delayed aka. Soft asserts for python

Few features:

    - No Dependenices on any other framework/library.
    - Should work with any testing framework.
    - Can be use as decorator or context manager.

![Sample](https://raw.githubusercontent.com/pr4bh4sh/delayed-assert/master/sample.jpg)

## Installation

### Install via pip

```bash
    pip install delayed-assert
```

### Install from master

```bash
    pip install git+https://github.com/pr4bh4sh/delayed-assert
```

## Uses

See `ExampleUnittest.py` for usage.

### Using assertion library with lambda

Pass the assertion call as

```python
    expect(lambda: self.assertListEqual([4,5,6,2,5],[7,8]))
```

While I've tested only with unittest asserttion,It should be able to use any assertion library.

Keep in mind that, Python does not support statement inside lambda, so

```python
    expect(lambda: assert 1 == 1)
```

won't work as it is not a valid lambda expression in python

### Current possible uses

```python
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

```

---------------

Credit : <http://pythontesting.net/strategy/delayed-assert/>
