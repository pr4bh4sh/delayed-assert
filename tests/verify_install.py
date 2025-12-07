import delayed_assert
import sys

print(f'Successfully imported delayed_assert from {delayed_assert.__file__}')

from delayed_assert import expect, assert_expectations, test_case, set_check_caller

# Verify basic functionality
# We must disable caller check because we are calling expect() from top-level scope
set_check_caller(False)
try:
    expect(1 == 1)
    assert_expectations()
    print('Basic functionality verification passed')
except Exception as e:
    print(f'Failed: {e}')
    sys.exit(1)
    
# Re-enable for decorator check (though decorator handles it regardless of flag? 
# No, decorator sets context, which expect() checks. Flag only matters if context/stack fails.)
set_check_caller(True)

# Verify @test_case matches
@test_case
def run_check():
    expect(1 == 1)
    
try:
    run_check()
    assert_expectations()
    print('Decorator verification passed')
except Exception as e:
    print(f'Decorator Failed: {e}')
    sys.exit(1)
