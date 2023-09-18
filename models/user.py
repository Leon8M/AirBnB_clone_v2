#!/usr/bin/python3
"""This module defines the User class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    """This class represents a user in the system"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance"""
        super().__init__(*args, **kwargs)
