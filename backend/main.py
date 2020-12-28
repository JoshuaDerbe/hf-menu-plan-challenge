# This is the main entry-point of the app that imports everything.
# This file is used to run the app.
from app import app, db

from models.admin import Admin
from models.customer import Customer
from models.ingredient import Ingredient
from models.inRecipe import InRecipe
from models.menu import Menu
from models.menuReview import MenuReview
from models.onMenu import OnMenu
from models.recipe import Recipe
from models.recipeReview import RecipeReview

from routes.general import *
from routes.ingredients import *

def create_tables():
    with db:
        # Create table for each model if it does not exist.
        db.create_tables([Admin,Customer,Ingredient,InRecipe,Menu,MenuReview,OnMenu,Recipe,RecipeReview])

if __name__ == "__main__":
    print("Creating tables...")
    create_tables()
    app.run(host="0.0.0.0", port="5000", debug=True)