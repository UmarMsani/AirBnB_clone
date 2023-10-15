#!/usr/bin/python3
"""
TEST Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_public_attributes(self):
        obj = Review()
        self.assertTrue(hasattr(obj, 'place_id'))
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(hasattr(obj, 'text'))

    def test_to_dict(self):
        obj = Review()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertFalse('place_id' in obj_dict)
        self.assertFalse('user_id' in obj_dict)
        self.assertFalse('text' in obj_dict)

if __name__ == "__main__":
    unittest.main()
