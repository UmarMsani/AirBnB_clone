#!/usr/bin/env python3
"""
User Class module
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Class for User objects, inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

