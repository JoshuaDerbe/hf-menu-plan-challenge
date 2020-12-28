from peewee import *

from models.base import BaseModel

# Model/Schema for Menus
class Menu(BaseModel):
    # name is a string restricted to 100 characters, and should be unique.
    name = CharField(null=False, unique=True, max_length=100)
    # start_date and end_date are dates (not Datetime) representing the starting
    # and ending date of the menu.
    start_date = DateField(null=False)
    end_date = DateField(null=False)
    