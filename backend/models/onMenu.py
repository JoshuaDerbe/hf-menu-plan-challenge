from peewee import *

from models.base import BaseModel
from models.menu import Menu
from models.recipe import Recipe

# This table holds the relationship between menus and recipes
# i.e. the recipes that are on specific menus.
class OnMenu(BaseModel):
    menu = ForeignKeyField(Menu, null=False)
    recipe = ForeignKeyField(Recipe, null=False)