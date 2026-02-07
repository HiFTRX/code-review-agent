import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def ask_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "")
    else:
        return f"Error contacting model: {response.text}"
