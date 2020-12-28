# File that creates the Flask instance and the database instance.
from flask import Flask
from peewee import *
from flask_praetorian import Praetorian


app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret"
app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 12}
app.config["JWT_REFRESH_LIFESPAN"] = {"days": 1}

# Create Postgres database
while 1:
    try:
        db = PostgresqlDatabase("hf_menu_plan", user="postgres", password="password", host="db", port=5432)
    except:
        print("Waiting for database...")
        time.sleep(1)
    else:
        break

print("Database connected!")

from models.user import User

# Initialize the flask-praetorian instance for the app
guard = Praetorian(app, user_class=User)