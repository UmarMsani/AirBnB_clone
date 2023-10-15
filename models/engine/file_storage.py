#!/usr/bin/python3
"""
FileStorage class module

"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): Object to set.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                loaded_objects = json.load(json_file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "User":
                        self.__objects[key] = User(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects, if it exists.

        Args:
            obj (BaseModel): Object to delete.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]

storage = FileStorage()
storage.reload()

