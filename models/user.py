#!/usr/bin/python3
"""Module that contains user information and
it inherits from BaseModel class"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class public attribute containing empty strings"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
