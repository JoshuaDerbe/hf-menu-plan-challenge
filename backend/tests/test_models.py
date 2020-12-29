"""
This file holds the unit tests for the models.
"""
import json

from app import app, db, guard

from models.user import User
from models.ingredient import Ingredient

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, roles and rolenames fields are defined correctly
    """
    assert new_user.email == "test@test.com"
    assert new_user.password != "password"
    assert new_user.roles == "user"
    assert new_user.rolenames == ["user"]

def test_new_ingredient():
    """
    GIVEN an Ingredient model
    WHEN a new Ingredient is created
    THEN check the fields are defined correctly
    """
    ingredient = Ingredient(name="tomato",energy=20,fat=0,carbs=0,fiber=0,protein=0,cholesterol=0,sodium=0)
    assert ingredient.name == "tomato"
    assert ingredient.energy == 20
    assert ingredient.fat == 0
    assert ingredient.carbs == 0
    assert ingredient.fiber == 0
    assert ingredient.protein == 0
    assert ingredient.cholesterol == 0
    assert ingredient.sodium == 0