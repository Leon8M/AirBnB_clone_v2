import unittest
from io import StringIO
import sys
import os
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    
    def setUp(self):
        """Redirect stdout to capture console output."""
        self.console_output = StringIO()
        sys.stdout = self.console_output
        self.console = HBNBCommand()

    def tearDown(self):
        """Restore stdout and cleanup."""
        sys.stdout = sys.__stdout__
        self.console_output.close()

    def test_quit_command(self):
        """Test the quit command."""
        with self.subTest():
            self.console.onecmd("quit")
            output = self.console_output.getvalue()
            self.assertEqual(output.strip(), "")
        
        with self.subTest():
            self.console.onecmd("EOF")
            output = self.console_output.getvalue()
            self.assertEqual(output.strip(), "")

    def test_help_command(self):
        """Test the help command."""
        with self.subTest():
            self.console.onecmd("help")
            output = self.console_output.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)
        
        with self.subTest():
            self.console.onecmd("help quit")
            output = self.console_output.getvalue()
            self.assertIn("Exits the program with formatting", output)

    # Add more test cases for other commands and functionalities of the console.

if __name__ == '__main__':
    unittest.main()
