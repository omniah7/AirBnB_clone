#!/usr/bin/python3
"""Amenity module containing attributes ssigned to amenities of place
and it inherits from BaseModel class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public attributes of amenity class"""
    name = ""
