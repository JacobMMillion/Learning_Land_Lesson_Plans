# Import the Flask class from the flask module
from flask import Flask, render_template

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def home():
    # This function returns the text that will be shown on the home page
    return render_template('index.html', message="Hello, World!")

# Check if the script is run directly (not imported) and run the app
if __name__ == '__main__':
    # Start the Flask web server
    app.run()