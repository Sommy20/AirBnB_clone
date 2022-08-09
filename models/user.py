#!/usr/bin/python3
""" Main User class """

import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
