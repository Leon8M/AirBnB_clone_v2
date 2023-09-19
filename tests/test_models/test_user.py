#!/usr/bin/python3
""" """
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of User"""
        user = User()
        self.assertIsInstance(user, User)

    def test_email_attribute(self):
        """Test if the email attribute is present"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))

    def test_password_attribute(self):
        """Test if the password attribute is present"""
        user = User()
        self.assertTrue(hasattr(user, 'password'))

    def test_first_name_attribute(self):
        """Test if the first_name attribute is present"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))

    def test_last_name_attribute(self):
        """Test if the last_name attribute is present"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))

    def test_created_updated_at(self):
        """Test created_at and updated_at attributes"""
        user = User()
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """Test to_dict() method"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['created_at'], user_dict['updated_at'])

    def test_str_representation(self):
        """Test __str__() method"""
        user = User()
        user_str = str(user)
        self.assertIsInstance(user_str, str)
        self.assertIn("[User]", user_str)
        self.assertIn("id: {}".format(user.id), user_str)

if __name__ == '__main__':
    unittest.main()
