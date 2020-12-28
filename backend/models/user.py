from peewee import *

from models.base import BaseModel

# Model/Schema for Users
# Note that user is a reserved table name for postgres
class User(BaseModel):
    # email is a string restricted to 100 characters, and should be unique.
    # No sophisticated checking for validity at the moment.
    email = CharField(null=False, unique=True, max_length=100)
    # password is a string restricted to 256 characters, that should be hashed
    password = CharField(null=False, max_length=256)
    # roles is a string of form "[role,role,...]"
    roles = CharField(null=False)

    class Meta:
        db_table = "user_table"
    
    @property
    def identity(self):
        """Get the unique identifier of a user
        This method is required by Flask-Praetorian
        Returns:
            int: The user's unique identifier
        """
        return self.id

    @property
    def rolenames(self):
        """Return the roles a given user has as a list of strings
        User roles should be stored as a single comma separated string
        This method is required by Flask-Praetorian
        Returns:
            List[str]: The list of rolenames
        """
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        """Find the user with a given email
        
        This method is required by Flask-Praetorian
        Args:
            cls: The class (table) to search for the user in
            email (str): The email to search for
        Returns:
            User: The user with the specified email
        """
        try:
            return cls.select().where(cls.email == email).get()
        except Exception:
            return None

    @classmethod
    def identify(cls, idx):
        """Find the user with a given id
        
        This method is required by Flask-Praetorian
        Args:
            cls: The class (table) to search for the user in
            idx (int): The id to search for
        Returns:
            User: The user with the specified id
        """
        try:
            return cls.select().where(cls.id == idx).get()
        except Exception:
            return None