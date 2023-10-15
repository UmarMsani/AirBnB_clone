#!/usr/bin/env python3
"""
Test for User module/class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class TestUser(unittest.TestCase):
    def test_instance_creation(self):
        obj = User()
        self.assertIsInstance(obj, User)

    def test_public_attributes(self):
        obj = User()
        self.assertTrue(hasattr(obj, 'email'))
        self.assertTrue(hasattr(obj, 'password'))
        self.assertTrue(hasattr(obj, 'first_name'))
        self.assertTrue(hasattr(obj, 'last_name'))

    def test_to_dict(self):
        obj = User()
        obj_dict = obj.to_dict()
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
