# This is the main entry-point of the app that imports everything.
# This file is used to run the app.
from app import app, db, guard

from models.user import User
from models.ingredient import Ingredient
from models.allergen import Allergen
from models.inRecipe import InRecipe
from models.menu import Menu
from models.menuReview import MenuReview
from models.onMenu import OnMenu
from models.recipe import Recipe
from models.recipeReview import RecipeReview

from routes.general import *
from routes.ingredients import *
from routes.users import *

def create_tables():
    with db:
        # Create table for each model if it does not exist.
        db.create_tables([User,Ingredient,Allergen,InRecipe,Menu,MenuReview,OnMenu,Recipe,RecipeReview])


if __name__ == "__main__":
    print("Creating tables...")
    create_tables()

    # Add a base admin if it does not already exist
    existing_admin = User.select().where(User.email == "admin@admin.com")
    if(not existing_admin.exists()):
        admin = User.create(email="admin@admin.com", password=guard.hash_password("password"), roles="admin")

    app.run(host="0.0.0.0", port="5000", debug=True)