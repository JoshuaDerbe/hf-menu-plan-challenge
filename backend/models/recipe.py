from peewee import *

from models.base import BaseModel

# Model/Schema for Recipes
class Recipe(BaseModel):
    # name is a string restricted to 100 characters, and should be unique.
    name = CharField(unique=True, max_length=100, null=False)
    # For simplicity steps will just be stored as a chunk of text with numbered
    # steps in it.
    steps = TextField(null=False)
    # prep_time is in minutes (rounded to nearest minute).
    prep_time = IntegerField(null=False, constraints = [Check("prep_time > 0")])
    # difficulty is a custom field that should only be "easy", "medium" 
    # or "hard".
    difficulty = CharField(null=False, constraints = [Check("difficulty='easy' OR difficulty='medium' OR difficulty='hard'")])
    