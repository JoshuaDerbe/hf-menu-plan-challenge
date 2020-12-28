from peewee import *

from models.base import BaseModel
from models.user import User
from models.menu import Menu

# This table holds the reviews/comments made by Users on Menus.
class MenuReview(BaseModel):
    menu = ForeignKeyField(Menu, null=False)
    user = ForeignKeyField(User, null=False)
    comment = CharField(max_length=500)
    # Rating should be 1, 2, 3, 4, or 5.
    rating = IntegerField(constraints = [Check("rating >= 1 AND rating <= 5")])

    class Meta:
        # A review should have either a comment, a rating, or both.
        constraints = [Check("comment != NULL OR rating != NULL")]