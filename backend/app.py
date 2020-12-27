# File that creates the Flask instance and the database instance.
from flask import Flask
from peewee import *

app = Flask(__name__)

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