from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Backend running",
        "service": "AI System Design Architect"
    })


# Architecture generation endpoint
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data or "idea" not in data:
        return jsonify({
            "error": "Missing 'idea' in request body"
        }), 400

    idea = data["idea"]

    # Placeholder structured response
    response = {
        "functional_requirements": ["User authentication"],
        "non_functional_requirements": ["Scalability"],
        "architecture_components": ["API Gateway", "Database"],
        "database_design": ["User table"],
        "scaling_strategy": ["Horizontal scaling"],
        "azure_mapping": ["Azure App Service"],
        "risks": ["Single point of failure"],
        "input_idea": idea
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)