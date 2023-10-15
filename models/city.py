#!/usr/bin/env python3
"""
City class module
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Class for City objects, inherits from BaseModel.
    """

    state_id = ""
    name = ""
