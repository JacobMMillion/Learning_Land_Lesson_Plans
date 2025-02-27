# Import the Flask class from the flask module
from flask import Flask, render_template

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def home():
    # This function returns the text that will be shown on the home page
    return render_template('index.html', message="Hello! This is the home page.")

# Route with a dynamic URL part that captures the name
@app.route('/<name>')
def greet(name):
    # Pass the name to the template to display it on the page
    return render_template('greet.html', name=name)

# Check if the script is run directly (not imported) and run the app
if __name__ == '__main__':
    # Start the Flask web server
    app.run()