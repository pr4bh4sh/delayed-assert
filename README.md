[![Build Status](https://travis-ci.org/pr4bh4sh/python-delayed-assert.svg?branch=master)](https://travis-ci.org/pr4bh4sh/delayed-assert)
[![PyPI version](https://badge.fury.io/py/delayed-assert.svg)](https://badge.fury.io/py/delayed-assert)
[![Downloads](https://pepy.tech/badge/delayed-assert)](https://pepy.tech/project/delayed-assert)
[![Downloads](https://pepy.tech/badge/delayed-assert/month)](https://pepy.tech/project/delayed-assert)

# Python-Delayed-Assert

Delayed aka. Soft asserts for python

Few features:

    - No Dependenices on any other framework/library.
    - Should work with any testing framework.
    - Can be use as decorator or context manager.

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

![Sample](https://raw.githubusercontent.com/pr4bh4sh/delayed-assert/master/sample.jpg)

---------------

Credit : <http://pythontesting.net/strategy/delayed-assert/>
