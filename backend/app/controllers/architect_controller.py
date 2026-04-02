from flask import request, jsonify

from app.services.architect_service import ArchitectService
from app.llm.ollama_provider import OllamaProvider

llm = OllamaProvider()
service = ArchitectService(llm)


def generate_architecture():
    data = request.get_json()

    # Validation
    if not data or "idea" not in data:
        return jsonify({"error": "Missing 'idea' in request"}), 400

    idea = data["idea"]

    # Call service
    result = service.generate_architecture(idea)

    return jsonify(result), 200