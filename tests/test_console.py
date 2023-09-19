import os
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.exc import OperationalError


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment and create initial database objects."""
        # Redirect stdout to capture console output
        cls.console_output = StringIO()
        cls.original_stdout = sys.stdout
        sys.stdout = cls.console_output

        # Initialize the HBNBCommand instance
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Restore stdout and clean up."""
        cls.console_output.close()
        sys.stdout = cls.original_stdout

    def setUp(self):
        """Create a fresh database session for each test."""
        storage.reload()

    def tearDown(self):
        """Clean up the database session after each test."""
        self.console_output = StringIO()  # Reset the captured output

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Test the create command with FileStorage."""
        # Test creating a City and User
        with patch('sys.stdout', new=StringIO()) as cout:
            self.console.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            self.console.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())

            self.console.onecmd('create User name="James" age=17 height=5.9')
            mdl_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            self.console.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'James'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """Test the create command with DBStorage."""
        # Test creating a User instance
        with patch('sys.stdout', new=StringIO()) as cout:
            clear_stream(cout)
            self.console.onecmd('create User email="john25@gmail.com" password="123"')
            mdl_id = cout.getvalue().strip()
            try:
                user = storage.get(User, mdl_id)
                self.assertIsNotNone(user)
                self.assertEqual(user.email, 'john25@gmail.com')
                self.assertEqual(user.password, '123')
            except Exception as e:
                self.fail(f"Error: {e}")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_show(self):
        """Test the show command with DBStorage."""
        # Test showing a User instance
        obj = User(email="john25@gmail.com", password="123")
        storage.new(obj)
        storage.save()

        with patch('sys.stdout', new=StringIO()) as cout:
            clear_stream(cout)
            self.console.onecmd('show User {}'.format(obj.id))
            self.assertIn("'name': 'john25@gmail.com'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())
