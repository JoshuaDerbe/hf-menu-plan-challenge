# File that holds the routes of the API i.e. maps urls to functions.
from app import app

@app.route('/')
def home():
   return "hello world!"