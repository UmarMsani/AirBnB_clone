#!/usr/bin/env python3
"""
Test for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime

class TestState(unittest.TestCase):
    def test_instance_creation(self):
        obj = State()
        self.assertIsInstance(obj, State)

    def test_public_attributes(self):
        obj = State()
        self.assertTrue(hasattr(obj, 'name'))

    def test_to_dict(self):
        obj = State()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertFalse('name' in obj_dict)

if __name__ == "__main__":
    unittest.main()
