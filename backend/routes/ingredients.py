# File that holds the routes related to ingredients.
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from json import dumps
from flask import *

from app import app

from models.ingredient import Ingredient

# Route to get the details of all ingredients in the database.
@app.route("/api/ingredients/", methods=["GET"])
def get_ingredients():
    ingredients = Ingredient.select()
    return jsonify({"results":[model_to_dict(ingredient) for ingredient in ingredients]})

# Route to the details of a list of specific ingredients in the database.
@app.route("/api/ingredients/", methods=["POST"])
def get_specific_ingredients():
    data = request.json
    if (data != None):
        id_list = data.get("ids")

    # Check the required fields are present.
    if (data == None or not isinstance(id_list, list)):
        abort(Response(dumps({"Error": "Request must be of the form: { ids: [str...]}"}), 400))

    # Retrieve the ingredients with matching ids.
    # The '<<' checks if the id is in the id list.
    # If an id is invalid an item is simply not returned.
    ingredients = Ingredient.select().where(Ingredient.id << id_list)

    return jsonify({"results":[model_to_dict(ingredient) for ingredient in ingredients]})

# Route to add an ingredient to the database.
@app.route("/api/ingredients/add/", methods=["POST"])
def add_ingredient(): 
    ingredient_data = request.json
    if (ingredient_data != None):
        name = ingredient_data.get("name")
        energy = ingredient_data.get("energy")

    # Check the required fields are present.
    if (ingredient_data == None or name == None or not isinstance(energy, int) or not energy >= 0):
        abort(Response(dumps({"Error": "Request must be of the form: { name: string, energy: (int >= 0)}"}), 400))

    # Check the ingredient doesn't already exist.
    existing_ingredient = Ingredient.select().where(Ingredient.name == name.lower())
    if (existing_ingredient.exists()):
        abort(Response(dumps({"Error": "An ingredient of this name already exists"}), 403))

    # Add the ingredient
    ingredient = Ingredient.create(name=name.lower(),energy=int(energy),fat=0,carbs=0,fiber=0,protein=0,cholesterol=0,sodium=0)

    return jsonify({"results":model_to_dict(ingredient)})

# Route to update an ingredient in the database.
@app.route("/api/ingredients/", methods=["PUT"])
def update_ingredient(): 
    ingredient_data = request.json
    if (ingredient_data != None):
        i_id = ingredient_data.get("id")
        name = ingredient_data.get("name")
        energy = ingredient_data.get("energy")

    # Check the required fields are present.
    if (ingredient_data == None or i_id == None):
        abort(Response(dumps({"Error": "Request must be of the form: { id: str, (optional: name: string, energy: int)}"}), 400))

    # Check the ingredient exists.
    existing_ingredient = Ingredient.select().where(Ingredient.id == i_id)
    if (not existing_ingredient.exists()):
        abort(Response(dumps({"Error": "An ingredient with this id does not exist"}), 403))

    existing_ingredient = existing_ingredient.get()

    # Update the ingredient
    if (name != None):
        # Check the new name isn't already taken
        existing_name = Ingredient.select().where(Ingredient.name == name.lower())
        if (existing_name.exists()):
            abort(Response(dumps({"Error": "An ingredient with this name already exists"}), 403))

        existing_ingredient.name = name.lower()

    if (energy != None):
        # Check energy is an integer >= 0
        if (not isinstance(energy, int) or not energy >= 0):
            abort(Response(dumps({"Error": "Energy must be an integer >= 0"}), 400))

        existing_ingredient.energy = energy

    existing_ingredient.save()

    return jsonify({"results":model_to_dict(existing_ingredient)})

# Route to remove an ingredient from the database.
@app.route("/api/ingredients/<i_id>", methods=["DELETE"])
def delete_ingredient(i_id): 
    # Check if the ingredient already exists.
    existing_ingredient = Ingredient.select().where(Ingredient.id == i_id)
    if (not existing_ingredient.exists()):
        abort(Response(dumps({"Error": "An ingredient of this id does not exist"}), 403))

    # Delete the ingredient.
    existing_ingredient.get().delete_instance()

    return "Successfully deleted ingredient with id {}.".format(i_id)
