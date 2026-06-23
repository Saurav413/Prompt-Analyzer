import re
import requests
import config

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {config.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": config.GROQ_MODEL, 
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    print("=== Sending to Groq ===")
    print("Payload model:", data["model"])

    session = requests.Session()
    session.trust_env = False
    r = session.post(GROQ_URL, headers=headers, json=data, timeout=config.GROQ_TIMEOUT)

    print("STATUS CODE:", r.status_code)
    print("RESPONSE:", r.text)

    r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]


def extract_score(text: str):
    """
    Extract a numeric score (0-10) from the model's response.
    """
    patterns = [
        r"(\d+)\s*/\s*10",
        r"score[:\s]*(\d+)",
    ]

    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            s = int(m.group(1))
            if 0 <= s <= 10:
                return s
    return None