#!/usr/bin/python3
"""
TEST AMINITY
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_str_representation(self):
        amenity = Amenity()
        expected_output = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_output)

if __name__ == "__main__":
    unittest.main()
