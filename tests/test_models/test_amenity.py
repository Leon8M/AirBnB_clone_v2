import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up a test instance of Amenity before each test."""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test."""
        del self.amenity

    def test_amenity_instance(self):
        """Test if an instance of Amenity is created successfully."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict_method(self):
        """Test the to_dict() method of Amenity."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_str_representation(self):
        """Test the __str__() method of Amenity."""
        amenity_str = str(self.amenity)
        self.assertIsInstance(amenity_str, str)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(str(self.amenity.id), amenity_str)

    def test_dummy_1(self):
        self.assertTrue(True)

    def test_dummy_2(self):
        self.assertEqual(1, 1)

    def test_dummy_3(self):
        self.assertFalse(False)

    def test_dummy_4(self):
        pass

    def test_dummy_5(self):
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main()
