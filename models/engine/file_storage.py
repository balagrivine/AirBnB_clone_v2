#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return self.__objects
        elif type(cls) == str:
            return {key: value for key, value in self.__objects.items() if value.__class__.__name__ == cls}
        else:
            return {key: value for key, value in self.__objects.items() if value.__class__ == cls}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""

        temp = {}
        for key, val in self.__objects.items():
            dict_val = temp.to_dict()
            temp.update({key: dict_val})
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """delete obj"""
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                obj_elem = json.load(f)
                for key, value in obj.elem.items():
                    clas = value["__class__"]
                    clas = eval(clas)
                    self.new(clas(**value))
        except FileNotFoundError:
            pass
