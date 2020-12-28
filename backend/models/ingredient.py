from peewee import *

from models.base import BaseModel

# Model/Schema for ingredients
class Ingredient(BaseModel):
    # name is a string restricted to 100 characters, and should be unique.
    name = CharField(null=False, unique=True, max_length=100)
    # energy in kJ
    energy = IntegerField(null=False, constraints = [Check("energy >= 0")])
    # fat, carbs, fiber, protein in g
    fat = DecimalField(null=False, constraints = [Check("fat >= 0")])
    carbs = DecimalField(null=False, constraints = [Check("carbs >= 0")])
    fiber = DecimalField(null=False, constraints = [Check("fiber >= 0")])
    protein = DecimalField(null=False, constraints = [Check("protein >= 0")])
    # cholesterol, sodium in mg
    cholesterol = DecimalField(null=False, constraints = [Check("cholesterol >= 0")])
    sodium = DecimalField(null=False, constraints = [Check("sodium >= 0")])

