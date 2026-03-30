import json


class ArchitectService:

    def __init__(self, llm):
        self.llm = llm

    def generate_architecture(self, idea: str):
        prompt = f"""
        You are a senior system design architect.

        Generate a system design for:
        {idea}

        Return ONLY valid JSON with:
        - functional_requirements
        - non_functional_requirements
        - architecture_components
        - database_design
        - scaling_strategy
        - azure_mapping
        - risks

        No explanation, only JSON.
        """

        response = self.llm.generate(prompt)

        try:
            return json.loads(response)
        except Exception as e:
            return {
                "error": "Invalid LLM response",
                "details": str(e)
            }