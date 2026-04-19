from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# -------------------------------
# 🔧 CLEAN AI OUTPUT
# -------------------------------
def clean_ai_output(data):
    try:
        # Fix typo like "nameiname"
        for item in data.get("functional_requirements", []):
            if "nameiname" in item:
                item["name"] = item.pop("nameiname")

        # Normalize non-functional requirements
        for item in data.get("non_functional_requirements", []):
            if "name" in item and "details" not in item:
                item["details"] = item["name"]

        return data
    except Exception:
        return data


# -------------------------------
# 🔁 FIX JSON USING AI
# -------------------------------
def fix_json_with_ai(bad_json):
    fix_prompt = f"""
    The following JSON is invalid. Fix it.

    RULES:
    - Return ONLY valid JSON
    - Do not add explanations
    - Fix syntax issues only

    Invalid JSON:
    {bad_json}
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": fix_prompt,
                "stream": False
            },
            timeout=120
        )

        return response.json().get("response", "").strip()

    except Exception:
        return bad_json


# -------------------------------
# 🏠 HEALTH CHECK
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Backend running",
        "service": "AI System Design Architect"
    })


# -------------------------------
# 🚀 GENERATE ENDPOINT
# -------------------------------
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data or "idea" not in data:
        return jsonify({"error": "Missing 'idea'"}), 400

    idea = data["idea"]

    # 🔥 STRICT PROMPT
    prompt = f"""
    You are a senior system design architect.

    Design a scalable system for: {idea}

    STRICT RULES:
    - Return ONLY valid JSON
    - Use double quotes everywhere
    - No trailing commas
    - No explanation text

    Return EXACT structure:

    {{
      "functional_requirements": [{{"name": "string"}}],
      "non_functional_requirements": [{{"name": "string", "details": "string"}}],
      "architecture_components": [{{"name": "string", "details": "string"}}],
      "database_design": [{{"componentName": "string", "tables": ["string"]}}],
      "scaling_strategy": [{{"description": "string"}}],
      "risks": [{{"name": "string"}}]
    }}
    """

    try:
        # -------------------------------
        # 📡 FIRST AI CALL
        # -------------------------------
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        raw_output = response.json().get("response", "").strip()

        # -------------------------------
        # 🧹 CLEAN RAW OUTPUT
        # -------------------------------
        raw_output = raw_output.replace("```json", "").replace("```", "").strip()

        # Extract JSON part
        start = raw_output.find("{")
        end = raw_output.rfind("}") + 1

        if start != -1 and end != -1:
            raw_output = raw_output[start:end]

        # -------------------------------
        # ✅ TRY PARSE
        # -------------------------------
        try:
            structured_output = json.loads(raw_output)
            structured_output = clean_ai_output(structured_output)
            return jsonify(structured_output), 200

        except json.JSONDecodeError:
            # -------------------------------
            # 🔁 FIX USING AI
            # -------------------------------
            fixed_output = fix_json_with_ai(raw_output)

            fixed_output = fixed_output.replace("```json", "").replace("```", "").strip()

            start = fixed_output.find("{")
            end = fixed_output.rfind("}") + 1

            if start != -1 and end != -1:
                fixed_output = fixed_output[start:end]

            try:
                structured_output = json.loads(fixed_output)
                structured_output = clean_ai_output(structured_output)
                return jsonify(structured_output), 200

            except json.JSONDecodeError:
                return jsonify({
                    "error": "JSON fixing failed",
                    "raw_output": raw_output,
                    "fixed_attempt": fixed_output
                }), 500

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Failed to connect to Ollama",
            "details": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Unexpected error",
            "details": str(e)
        }), 500


# -------------------------------
# ▶️ RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)