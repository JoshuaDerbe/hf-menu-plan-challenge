# This is the main entry-point of the app that imports everything.
# This file is used to run the app.
from app import app, db

from models.ingredient import Ingredient
from routes import *

def create_tables():
    with db:
        # Create table for each model if it does not exist
        db.create_tables([Ingredient])

if __name__ == "__main__":
    print("Creating tables...")
    create_tables()
    app.run(host="0.0.0.0", debug=True)