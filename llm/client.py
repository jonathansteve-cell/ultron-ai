import os
import requests
from dotenv import load_dotenv
from llm.schemas import LLMResponse, LLMMessage
from llm.prompts import ULTRON_SYSTEM_PROMPT

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta")

def call_llm(system_prompt: str, user_message: str) -> LLMResponse:
    if LLM_PROVIDER == "google":
        url = f"{LLM_BASE_URL}/models/gemini-2.0-pro:generateContent?key={GOOGLE_API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"{system_prompt}\n\nUser: {user_message}"}]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 512
            }
        }
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        return LLMResponse(message=LLMMessage(role="assistant", content=text))
    else:
        return LLMResponse(
            message=LLMMessage(
                role="assistant",
                content=f"[Mock LLM] You said: {user_message}"
            )
        )
