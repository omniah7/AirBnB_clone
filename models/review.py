#!/usr/bin/python3
"""Review module contains various attributes assigned to reviews
and it inherits from BaseModel Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class containing various public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
