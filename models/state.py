#!/usr/bin/python3
"""
class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class State
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
