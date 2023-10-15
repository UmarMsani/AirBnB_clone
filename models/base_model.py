#!/usr/bin/python3
"""BaseModel Class Which all Will inhirt from it."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defining all common attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """Initalizing an instance."""
        if kwargs is not None and len(kwargs) != 0:
            if 'class' in kwargs:
                del kwargs['class']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
def to_dict(self):
        """returning the dictionary representation of instance."""
        my_dict = dict(self.__dict__)
        my_dict.update({'__class__': self.__class__.__name__,
                        'created_at': self.created_at.isoformat(),
                        'id': self.id,
                        'updated_at': self.updated_at.isoformat()})
        return my_dict

    def __str__(self):
        """The string representation."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"


