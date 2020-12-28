from peewee import *

from models.base import BaseModel
from models.recipe import Recipe
from models.ingredient import Ingredient

# This table holds the relationship between ingredients and recipes
# i.e. the ingredients that are in specific recipes, and the measurement.
class InRecipe(BaseModel):
    ingredient = ForeignKeyField(Ingredient, null=False)
    recipe = ForeignKeyField(Recipe, null=False)
    # As measurement could be in different units, for now it will be a string.
    measurement = CharField(null=False, max_length=100)