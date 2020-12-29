from peewee import *

from models.base import BaseModel
from models.user import User
from models.recipe import Recipe

# This table holds the reviews/comments made by Users on Recipes.
class RecipeReview(BaseModel):
    recipe = ForeignKeyField(Recipe, null=False)
    user = ForeignKeyField(User, null=False)
    # comment is a string of max length 500 characters.
    comment = CharField(max_length=500)
    # Rating should be 1, 2, 3, 4, or 5.
    rating = IntegerField(constraints = [Check("rating >= 1 AND rating <= 5")])

    class Meta:
        # A review should have either a comment, a rating, or both.
        constraints = [Check("comment != NULL OR rating != NULL")]
        # As it is not clear from the spec, we assume a customer can only leave
        # one review for a specific recipe.
        # As such, recipe and user together should be the primary key.
        # There should never be two rows with the same recipe and user.
        primary_key = CompositeKey("recipe", "user")