import sys

if sys.version_info > (3, 0):  # Python 3 and above
    from delayed_assert.delayed_assert import expect, assert_expectations
else:  # for Python 2 
    from delayed_assert import expect, assert_expectations
