import google.generativeai as genai
from agno.agent import Agent
from config import GEMINI_API_KEY, SYSTEM_PROMPT
from chat import GeminiChat

# Initialize Gemini chat model
gemini_chat = GeminiChat(api_key=GEMINI_API_KEY)

agent = Agent(
    model=gemini_chat,
    tools=[],
    instructions=SYSTEM_PROMPT,
    markdown=True,
)

def get_recipe(user_input: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input},
    ]
    response = agent.model.chat(messages)
    return response

import requests
from config import EXA_API_KEY

def get_real_recipes(query: str):
    url = "https://api.exa.ai/search"
    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "query": query,
        "num_results": 6,
    }
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception:
        return []

    recipes = []
    for r in data.get("results", []):
        recipes.append({
            "title": r.get("title", "Untitled"),
            "url": r.get("url", "#"),
            "author": r.get("author", ""),
            "published": r.get("publishedDate", "")[:10],
            "image": r.get("image", None),
        })
    return recipes
