# Import the Flask library
from flask import Flask

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def home():
    # This function returns the text that will be shown on the home page
    return "HELLO!!! THIS IS A HOME PAGE!!!! YAY :)"


# WHAT RUNS
app.run()