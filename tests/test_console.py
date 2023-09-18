import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
import re

from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'FileStorage test')
    def test_create_db(self):
        """Test create command with database storage."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User email='test@example.com' password='123'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', output))
            self.assertIn('User', output)
            self.assertTrue(storage.get("User", output))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'FileStorage test')
    def test_show_db(self):
        """Test show command with database storage."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User email='test@example.com' password='123'")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"show User {obj_id}")
            output = mock_stdout.getvalue().strip()
            self.assertIn(obj_id, output)
            self.assertIn("test@example.com", output)
            self.assertIn("123", output)

    def test_create_file(self):
        """Test create command with file storage."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User email='test@example.com' password='123'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', output))
            self.assertIn('User', output)
            self.assertTrue(storage.get("User", output))

    def test_show_file(self):
        """Test show command with file storage."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User email='test@example.com' password='123'")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"show User {obj_id}")
            output = mock_stdout.getvalue().strip()
            self.assertIn(obj_id, output)
            self.assertIn("test@example.com", output)
            self.assertIn("123", output)

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("quit")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("EOF")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()
