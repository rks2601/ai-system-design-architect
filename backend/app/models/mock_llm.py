import json
from app.models.base_llm import BaseLLM


class MockLLM(BaseLLM):

    def generate(self, prompt: str) -> str:
        response = {
            "functional_requirements": [
                "User authentication",
                "Photo upload",
                "Feed generation"
            ],
            "non_functional_requirements": [
                "Scalability",
                "High availability"
            ],
            "architecture_components": [
                "API Gateway",
                "Load Balancer",
                "Microservices"
            ],
            "database_design": [
                "User table",
                "Posts table"
            ],
            "scaling_strategy": [
                "Horizontal scaling",
                "CDN usage"
            ],
            "azure_mapping": [
                "Azure App Service",
                "Azure Blob Storage"
            ],
            "risks": [
                "Single point of failure"
            ]
        }

        return json.dumps(response)