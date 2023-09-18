#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """A class representing a User."""
    
    _tablename_ = 'users'  # Table name
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    # Add relationship with Place
    places = relationship('Place', backref='user', cascade='all, delete-orphan')
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")

