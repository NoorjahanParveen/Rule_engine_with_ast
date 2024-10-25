from flask import Flask
from flask_cors import CORS  # Import CORS

def create_app():
    app = Flask(__name__,
                template_folder='../templates',  # Adjust path to templates folder
                static_folder='../static')

    # Enable CORS for all routes
    CORS(app)  # This will enable CORS for all domains

    # Import and register blueprints or routes here
    from routes import main as routes
    app.register_blueprint(routes)

    return app
