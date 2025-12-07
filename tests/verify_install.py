import delayed_assert
import sys

print(f'Successfully imported delayed_assert from {delayed_assert.__file__}')

from delayed_assert import expect, assert_expectations, test_case

# Verify basic functionality
try:
    expect(1 == 1)
    assert_expectations()
    print('Basic functionality verification passed')
except Exception as e:
    print(f'Failed: {e}')
    sys.exit(1)

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
