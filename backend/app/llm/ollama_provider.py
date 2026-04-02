import requests
from app.llm.base import BaseLLM


class OllamaProvider(BaseLLM):

    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code != 200:
            raise Exception("Ollama request failed")

        data = response.json()

        return data["response"]