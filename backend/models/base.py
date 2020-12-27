from peewee import *

from app import db

# Base model class that specifies which database to use so any subclasses will
# automatically use the correct storage
class BaseModel(Model):
    class Meta:
        database = db
