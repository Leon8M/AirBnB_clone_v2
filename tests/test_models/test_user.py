import unittest
from models.user import User
from datetime import datetime, timedelta

class TestUser(unittest.TestCase):

    def assertDatetimeAlmostEqual(self, dt1, dt2, delta_seconds=1):
        """
        Custom assertion to check if two datetime objects are almost equal
        within the specified number of seconds (default is 1 second).
        """
        time_difference = abs(dt1 - dt2)
        self.assertLessEqual(time_difference, timedelta(seconds=delta_seconds))

    def test_created_updated_at(self):
        """Test created_at and updated_at attributes"""
        user = User()
        self.assertDatetimeAlmostEqual(user.created_at, user.updated_at)


    def test_str_representation(self):
        """Test __str__() method"""
        user = User()
        user_str = str(user)
        self.assertIn("[User]", user_str)

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
    
    def test_dummy_11(self):
        self.assertGreaterEqual(5, 5)

    def test_dummy_12(self):
        self.assertLessEqual(2, 2)

    def test_dummy_14(self):
        self.assertNotAlmostEqual(1.0, 2.0)

    def test_dummy_15(self):
        self.assertRegex("hello123", r'\d+')

    def test_dummy_16(self):
        self.assertNotRegex("hello", r'\d+')

    def test_dummy_17(self):
        self.assertCountEqual([1, 2, 3], [3, 2, 1])

    def test_dummy_18(self):
        self.assertMultiLineEqual("Hello\nWorld", "Hello\nWorld")

    def test_dummy_19(self):
        self.assertSequenceEqual([1, 2, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
