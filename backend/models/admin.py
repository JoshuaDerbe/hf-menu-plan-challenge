from peewee import *

from models.base import BaseModel

# Model/Schema for Admins
class Admin(BaseModel):
    # email is a string restricted to 100 characters, and should be unique.
    # No sophisticated checking for validity at the moment.
    email = CharField(null=False, unique=True, max_length=100)
    # password is a string restricted to 100 characters.
    password = CharField(null=False, max_length=100)
    