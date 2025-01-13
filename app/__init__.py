from flask import Flask
from .routes import support_routes

def create_app():
    app = Flask(__name__, root_path="C:/Users/CSO-II/Documents/mishes projects/ai_tech_support")
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(support_routes)

    return app
