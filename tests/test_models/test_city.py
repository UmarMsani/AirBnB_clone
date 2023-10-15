#!/usr/bin/env python3
"""
Test for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        obj = City()
        self.assertIsInstance(obj, City)

    def test_public_attributes(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'state_id'))
        self.assertTrue(hasattr(obj, 'name'))

    def test_to_dict(self):
        obj = City()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertFalse('state_id' in obj_dict)
        self.assertFalse('name' in obj_dict)
