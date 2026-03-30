from flask import Blueprint
from app.controllers.architect_controller import generate_architecture

architect_bp = Blueprint("architect", __name__)


@architect_bp.route("/", methods=["GET"])
def home():
    return {"status": "Backend running"}


@architect_bp.route("/generate", methods=["POST"])
def generate():
    return generate_architecture()