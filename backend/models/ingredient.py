from peewee import *

from models.base import BaseModel

# Model/Schema for ingredients
class Ingredient(BaseModel):
    name = CharField(unique=True)
