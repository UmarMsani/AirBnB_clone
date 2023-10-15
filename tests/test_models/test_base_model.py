#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)

    def test_save(self):
        obj = BaseModel()
        created_at_before = obj.created_at
        obj.save()
        self.assertNotEqual(created_at_before, obj.updated_at)

    def test_str(self):
        obj = BaseModel()
        self.assertEqual(str(obj), f"[BaseModel] ({obj.id}) {obj.__dict__}")

    def test_created_at_type(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_type(self):
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
