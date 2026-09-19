import json
import requests

def query_ollama(prompt: str, model: str = "deepseek-r1:8b") -> str:
    """Sends prompt directly to local Ollama API and enforces JSON output."""
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": "json"
    }
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]