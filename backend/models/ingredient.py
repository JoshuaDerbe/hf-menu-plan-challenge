from peewee import *

from models.base import BaseModel

# Model/Schema for ingredients
class Ingredient(BaseModel):
    # name is a string restricted to 100 characters, and should be unique.
    name = CharField(null=False, unique=True, max_length=100)
    # energy in kJ
    energy = IntegerField(default=0, constraints = [Check("energy >= 0")])
    # fat, carbs, fiber, protein in g
    fat = IntegerField(default=0, constraints = [Check("fat >= 0")])
    carbs = IntegerField(default=0, constraints = [Check("carbs >= 0")])
    fiber = IntegerField(default=0, constraints = [Check("fiber >= 0")])
    protein = IntegerField(default=0, constraints = [Check("protein >= 0")])
    # cholesterol, sodium in mg
    cholesterol = IntegerField(default=0, constraints = [Check("cholesterol >= 0")])
    sodium = IntegerField(default=0, constraints = [Check("sodium >= 0")])

