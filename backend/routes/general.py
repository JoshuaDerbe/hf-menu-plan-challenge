# File that holds the general routes of the API.
from app import app

@app.route('/')
def warning():
   return "Ensure routes begin with /api!"

@app.route('/api')
def home():
   return "Hello world!"