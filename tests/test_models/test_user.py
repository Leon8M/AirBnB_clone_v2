import unittest
from models.user import User
from datetime import datetime, timedelta

class TestUser(unittest.TestCase):

    def test_created_updated_at(self):
        """Test created_at and updated_at attributes"""
        user = User()
        time_difference = user.updated_at - user.created_at
        self.assertTrue(time_difference < timedelta(seconds=1))  # Adjust tolerance as needed

    def test_to_dict(self):
        """Test to_dict() method"""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['created_at'], user_dict['updated_at'])

    def test_str_representation(self):
        """Test __str__() method"""
        user = User()
        user_str = str(user)
        self.assertIn("[User]", user_str)
        self.assertIn("id: {}".format(user.id), user_str)

    def test_email_attribute(self):
        """Test email attribute"""
        user = User(email="test@example.com")
        self.assertEqual(user.email, "test@example.com")

    def test_password_attribute(self):
        """Test password attribute"""
        user = User(password="mypassword")
        self.assertEqual(user.password, "mypassword")

    def test_first_name_attribute(self):
        """Test first_name attribute"""
        user = User(first_name="John")
        self.assertEqual(user.first_name, "John")

    def test_last_name_attribute(self):
        """Test last_name attribute"""
        user = User(last_name="Doe")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
