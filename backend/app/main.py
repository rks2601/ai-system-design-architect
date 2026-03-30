from flask import Flask
from flask_cors import CORS

from app.routes.architect_routes import architect_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register Blueprint (routes)
    app.register_blueprint(architect_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)