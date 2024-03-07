#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        formatted_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            formatted_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(formatted_dictionary, fileJSON, indent=4)

    def reload(self):
        try:
            new__objects = {}
            with open(FileStorage.__file_path, "r") as fileJSON:
                new__objects = json.load(fileJSON)
                for obj in new__objects.values():
                    class_name = obj["__class__"]
                    if class_name in class_mapping:
                        self.new(class_mapping[class_name](**obj))
        except FileNotFoundError:
            pass

