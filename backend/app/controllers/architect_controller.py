from flask import request, jsonify

from app.services.architect_service import ArchitectService
from app.models.mock_llm import MockLLM

# Initialize dependencies
llm = MockLLM()
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