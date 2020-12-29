from peewee import *

from models.base import BaseModel
from models.menu import Menu
from models.recipe import Recipe

# This table holds the relationship between menus and recipes
# i.e. the recipes that are on specific menus.
class OnMenu(BaseModel):
    menu = ForeignKeyField(Menu, null=False)
    recipe = ForeignKeyField(Recipe, null=False)

    class Meta:
        # menu and recipe together should be the primary key.
        # There should never be two rows with the same menu and recipe.
        primary_key = CompositeKey("menu", "recipe")