import unittest
import sys
import os
import subprocess

class TestOptionalCallerCheck(unittest.TestCase):
    
    def test_delayed_assert_caller_check(self):
        """
        Verify that we can disable the caller stack check.
        Runs a separate process to ensure 'test' is not in the stack frame.
        """
        # Create a temporary script to run
        script_content = """
import sys
import os
# Add parent dir to path so we can import delayed_assert
sys.path.insert(0, os.getcwd())

from delayed_assert import expect, assert_expectations
from delayed_assert.delayed_assert import set_check_caller

class StandaloneRunner:
    def run_check(self):
        expect(1 == 2, "Failure")
        assert_expectations()

def main():
    # 1. Verify default behavior raises Exception
    wrapper = StandaloneRunner()
    try:
        wrapper.run_check()
    except Exception as e:
        if "Could not identify test method" not in str(e):
             sys.exit(1) # Unexpected exception
    else:
        sys.exit(2) # Knew it should fail but didn't

    # 2. Verify disabling check allows it to run
    set_check_caller(False)
    try:
        wrapper.run_check()
    except AssertionError as e:
        if "Failure" in str(e):
            sys.exit(0) # Success
        sys.exit(3) # Wrong assertion error
    except Exception as e:
        sys.exit(4) # Unexpected exception

if __name__ == "__main__":
    main()
"""
        # Write script to file
        with open('temp_verify_issue_15.py', 'w') as f:
            f.write(script_content)
        
        try:
            # Run the script
            result = subprocess.run(
                [sys.executable, 'temp_verify_issue_15.py'],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("Subprocess stdout:", result.stdout)
                print("Subprocess stderr:", result.stderr)
                
            self.assertEqual(result.returncode, 0, 
                f"Verification script failed with code {result.returncode}")
                
        finally:
            if os.path.exists('temp_verify_issue_15.py'):
                os.remove('temp_verify_issue_15.py')

if __name__ == '__main__':
    unittest.main()
