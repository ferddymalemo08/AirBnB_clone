#!/usr/bin/python3
"""Defines the BaseModel class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
    """
    tformat = "%Y-%m-%dT%H:%M:%S.%f"
    self.id = str(uuid4())
    self.created_at = datetime.today()
    self.updated_at = datetime.today()

    if len(kwargs) != 0:
        for k, v in kwargs.items():
            if k == "created_at" or k == "updated_at":
                self.__dict__[k] = datetime.strptime(v, tformat)
            else:
                self.__dict__[k] = v
    else:
        models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Include the key/value pair __class__ representing
        the class name of the object.
        """
        ourdict = self.__dict__.copy()
        ourdict["created_at"] = self.created_at.isoformat()
        ourdict["updated_at"] = self.updated_at.isoformat()
        ourdict["__class__"] = self.__class__.__name__
        return ourdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
