#!/usr/bin/python3
"""Module for City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City"""
    state_id = ""
    name = ""
