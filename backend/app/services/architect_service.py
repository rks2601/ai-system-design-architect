import json
import re

class ArchitectService:

    def __init__(self, llm):
        self.llm = llm

    def extract_json(self, text):
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return match.group(0) if match else None

    def generate_architecture(self, idea: str):
        prompt = f"""
        You are a senior system design architect.

        Design a highly scalable system for:
        {idea}

        Think like a real system design interview.

        IMPORTANT:
        - Include backend, database, caching, CDN, and messaging systems
        - Consider millions of users and high traffic
        - Be detailed and practical

        Return ONLY valid JSON.

        Format:

        {{
        "functional_requirements": [],
        "non_functional_requirements": [],
        "architecture_components": [],
        "database_design": [],
        "scaling_strategy": [],
        "azure_mapping": [],
        "risks": []
        }}

        Rules:
        - Each section must have 5–8 items
        - Include advanced components like:
        - CDN
        - Cache (Redis)
        - Message Queue
        - Media Storage
        - Be specific (not generic)
        """

        response = self.llm.generate(prompt)

        #  DEBUG (IMPORTANT)
        print("\n RAW LLM RESPONSE:\n", response)

        # ✅ Extract JSON
        clean_json = self.extract_json(response)

        if not clean_json:
            return {
                "error": "No JSON found in LLM response",
                "raw": response
            }

        try:
            return json.loads(clean_json)
        except Exception as e:
            return {
                "error": "Invalid JSON after extraction",
                "raw": clean_json,
                "details": str(e)
            }