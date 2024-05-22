import os
from flask import Flask
from .config import Config

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from the config object
app.config.from_object(Config)

# Register blueprints (ensures views are imported after app initialization)
from .views import views
app.register_blueprint(views)

# Function to load the model (if applicable)

# Ensure this script runs only when executed directly and not when imported
if __name__ == "__main__":
    app.run(debug=True)  # debug=True enables debug mode (use cautiously in production)
