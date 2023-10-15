#!/usr/bin/python3
"""
TEST
"""
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def test_instance_creation(self):
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_public_attributes(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'city_id'))
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(hasattr(obj, 'description'))
        self.assertTrue(hasattr(obj, 'number_rooms'))
        self.assertTrue(hasattr(obj, 'number_bathrooms'))
        self.assertTrue(hasattr(obj, 'max_guest'))
        self.assertTrue(hasattr(obj, 'price_by_night'))
        self.assertTrue(hasattr(obj, 'latitude'))
        self.assertTrue(hasattr(obj, 'longitude'))
        self.assertTrue(hasattr(obj, 'amenity_ids'))

    def test_to_dict(self):
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertFalse('city_id' in obj_dict)
        self.assertFalse('user_id' in obj_dict)
        self.assertFalse('name' in obj_dict)
        self.assertFalse('description' in obj_dict)
        self.assertFalse('number_rooms' in obj_dict)
        self.assertFalse('number_bathrooms' in obj_dict)
        self.assertFalse('max_guest' in obj_dict)
        self.assertFalse('price_by_night' in obj_dict)
        self.assertFalse('latitude' in obj_dict)
        self.assertFalse('longitude' in obj_dict)
        self.assertFalse('amenity_ids' in obj_dict)
