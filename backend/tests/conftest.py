"""
This file holds the fixtures for the pytests
"""
import pytest

from app import app, db, guard

from models.user import User
from models.ingredient import Ingredient

@pytest.fixture(scope="module")
def new_user():
    user = User(email="test@test.com", password=guard.hash_password("password"), roles="user")
    return user