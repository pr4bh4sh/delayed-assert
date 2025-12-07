import unittest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from delayed_assert import expect, assert_expectations
from delayed_assert.delayed_assert import set_color_enabled, get_color_enabled


class TestColorToggle(unittest.TestCase):
    """Test cases for color toggle functionality."""
    
    def setUp(self):
        """Save original color state before each test."""
        self.original_state = get_color_enabled()
    
    def tearDown(self):
        """Restore original color state after each test."""
        set_color_enabled(self.original_state)
    
    def test_color_enabled_output_has_ansi_codes(self):
        """Test that output contains ANSI codes when colors are enabled."""
        set_color_enabled(True)
        
        expect(1 == 2, "Test failure")
        
        try:
            assert_expectations()
            self.fail("Should have raised AssertionError")
        except AssertionError as e:
            output = str(e)
            self.assertIn('\033[', output, "Should contain ANSI codes when enabled")
            self.assertIn('Test failure', output)
    
    def test_color_disabled_output_has_no_ansi_codes(self):
        """Test that output does NOT contain ANSI codes when colors are disabled."""
        set_color_enabled(False)
        
        expect(1 == 2, "Test failure")
        
        try:
            assert_expectations()
            self.fail("Should have raised AssertionError")
        except AssertionError as e:
            output = str(e)
            self.assertNotIn('\033[', output, "Should NOT contain ANSI codes when disabled")
            self.assertIn('Test failure', output)
    
    def test_toggle_colors(self):
        """Test that colors can be toggled on and off."""
        set_color_enabled(True)
        self.assertTrue(get_color_enabled())
        
        set_color_enabled(False)
        self.assertFalse(get_color_enabled())


if __name__ == '__main__':
    unittest.main(verbosity=2)
