# File that holds the routes related to users.
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from json import dumps
from flask import *
import flask_praetorian

from app import app, guard

from models.user import User


# Route to add a user to the database.
@app.route("/api/signup/", methods=["POST"])
def add_user(): 
    user_data = request.json
    if (user_data != None):
        email = user_data.get("email")
        password = user_data.get("password")

    # Check the required fields are present.
    if (user_data == None or email == None or password == None):
        abort(Response(dumps({"Error": "Request must be of the form: { email: str, password: str }"}), 400))

    # Check the user doesn't already exist.
    existing_user = User.select().where(User.email == email.lower())
    if (existing_user.exists()):
        abort(Response(dumps({"Error": "A user with this email already exists"}), 403))

    # Add the user
    user = User.create(email=email.lower(), password=guard.hash_password(password), roles="user")

    return jsonify({"results": {"id": user.id, "email": user.email}})

@app.route("/api/login/", methods=["POST"])
def login():
    user_data = request.json
    if (user_data != None):
        email = user_data.get("email")
        password = user_data.get("password")

    # Check the required fields are present
    if (user_data == None or email == None or password == None):
        abort(Response(dumps({"Error": "Request must be of the form: { email: str, password: str }"}), 400))

    user = guard.authenticate(email, password)
    return jsonify({"access_token": guard.encode_jwt_token(user), "roles": user.roles})

# Route to delete a user from the database.
@app.route("/api/users/<u_id>", methods=["DELETE"])
@flask_praetorian.roles_required("admin")
def delete_user(u_id): 
    # Check if the user already exists.
    existing_user = User.select().where(User.id == u_id)
    if (not existing_user.exists()):
        abort(Response(dumps({"Error": "A user with this id does not exist"}), 403))

    # Delete the user.
    existing_user.get().delete_instance()

    return "Successfully deleted user with id {}.".format(u_id)