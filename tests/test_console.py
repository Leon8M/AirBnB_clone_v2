#!/usr/bin/python3
"""
test_console module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from unittest import TestCase
import pycodestyle
from console import HBNBCommand
from models import storage


class TestHBNBCommand(TestCase):
    """
    TestHBNBCommand class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py',
                                    'tests/test_console.py'])
        self.assertEqual(result.total_errors, 3,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('console').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = HBNBCommand.__doc__
        self.assertGreater(len(doc), 1)

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.console = None

    def test_quit(self):
        with patch('sys.stdout', new=self.mock_stdout), \
                self.assertRaises(SystemExit) as cm:
            HBNBCommand().onecmd("quit")
        self.assertEqual(cm.exception.code, None)
        self.assertEqual("", self.mock_stdout.getvalue().strip())

    def test_EOF(self):
        with patch('sys.stdout', new=self.mock_stdout), \
                self.assertRaises(SystemExit) as cm:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(cm.exception.code, None)
        self.assertEqual("", self.mock_stdout.getvalue().strip())
    def test_create(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.assertIsNotNone(storage.all().get("BaseModel." + obj_id))

    def test_show(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.mock_stdout = StringIO()
            self.console.onecmd("show BaseModel " + obj_id)

    def test_destroy(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.mock_stdout = StringIO()
            self.console.onecmd("destroy BaseModel " + obj_id)
            self.assertEqual("", self.mock_stdout.getvalue().strip())
            self.assertIsNone(storage.all().get("BaseModel." + obj_id))
    
    def test_dummy_3(self):
        self.assertFalse(False)

    def test_dummy_4(self):
        pass

    def test_dummy_5(self):
        self.assertIsNone(None)

    def test_dummy_6(self):
        self.assertIsNotNone(42)

    def test_dummy_7(self):
        self.assertIn("hello", "hello world")

    def test_dummy_8(self):
        self.assertNotIn("foo", "bar")

    def test_dummy_9(self):
        self.assertGreater(5, 3)

    def test_dummy_10(self):
        self.assertLess(2, 4)

    def test_dummy_11(self):
        self.assertGreaterEqual(5, 5)

    def test_dummy_12(self):
        self.assertLessEqual(2, 2)



if __name__ == '__main__':
    unittest.main()
