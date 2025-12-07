import unittest
import sys
import os
import subprocess

class TestIssue33Decorator(unittest.TestCase):
    
    def test_decorator_works_standalone(self):
        """
        Verify that @test_case allows expect() usage in functions not named 'test*',
        even when caller check is ENABLED (default).
        """
        script_content = """
import sys
import os
sys.path.insert(0, os.getcwd())

from delayed_assert import expect, assert_expectations
from delayed_assert.delayed_assert import test_case

@test_case
def verify_something():
    expect(1 == 2, "Failure 1")

def main():
    try:
        verify_something()
        assert_expectations()
    except AssertionError as e:
        if "Failure 1" in str(e):
            sys.exit(0)
        else:
            print(f"Wrong assertion error: {e}")
            sys.exit(2)
    except Exception as e:
        print(f"Unexpected exception: {e}")
        sys.exit(3)
        
    print("Should have raised AssertionError")
    sys.exit(4)

if __name__ == "__main__":
    main()
"""
        with open('temp_verify_issue_33.py', 'w') as f:
            f.write(script_content)
            
        try:
            result = subprocess.run(
                [sys.executable, 'temp_verify_issue_33.py'],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("Subprocess stdout:", result.stdout)
                print("Subprocess stderr:", result.stderr)
                
            self.assertEqual(result.returncode, 0, 
                f"Verification script failed with code {result.returncode}")
        finally:
            if os.path.exists('temp_verify_issue_33.py'):
                os.remove('temp_verify_issue_33.py')

if __name__ == '__main__':
    unittest.main()
