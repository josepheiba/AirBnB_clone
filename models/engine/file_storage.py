#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
    """
    def save(self):
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(FileStorage.__objects, fileJSON, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fileJSON:
                FileStorage.__objects = json.load(fileJSON)
        except FileNotFoundError:
            pass
    """

    def save(self):
        formatted_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            formatted_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(formatted_dictionary, fileJSON, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fileJSON:
                temp_dict = json.load(fileJSON)
                for key, value in temp_dict.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
