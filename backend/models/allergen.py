from peewee import *

from models.base import BaseModel
from models.ingredient import Ingredient

# This table holds the relationship between ingredients and allergens, which
# is a multi valued attribute.
# e.g. dairy, egg, gluten, etc
class Allergen(BaseModel):
    ingredient = ForeignKeyField(Ingredient, null=False)
    allergen = CharField(null=False)

    class Meta:
        # Ingredient and allergen together should be the primary key.
        # There should never be two rows with the same ingredient and allergen.
        primary_key = CompositeKey("ingredient", "allergen")