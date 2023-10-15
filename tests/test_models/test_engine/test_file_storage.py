#!/usr/bin/env python3
"""
Test for FileStorage module
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue(obj.__class__.__name__ + '.' + obj.id in self.storage.all())

    def test_save_method(self):
        obj = BaseModel()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_reload_method(self):
        obj = BaseModel()
        obj.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertTrue(obj.__class__.__name__ + '.' + obj.id in all_objs)

    def test_save_method_user(self):
        obj = User()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_save_method_state(self):
        obj = State()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_save_method_city(self):
        obj = City()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_save_method_amenity(self):
        obj = Amenity()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_save_method_place(self):
        obj = Place()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

    def test_save_method_review(self):
        obj = Review()
        obj.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, data)

if __name__ == '__main__':
    unittest.main()
