import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import re

load_dotenv()

api_key = st.secrets["OPENAI_API_KEY"]
print(api_key)
base_url = st.secrets["OPENAI_BASE_URL"]

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    default_headers={
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8501/",
        "X-Title": "Aicade Code Iterator AI"
    }
)

def modify_code(code_input, user_prompt):
    messages = [
    {
        "role": "system",
        "content": (
            "You are a Python coding assistant specialized in game development.\n"
            "Return only the Python code that was modified based on the user's request.\n"
            "When making changes to game code, ensure the logic aligns with common game development practices.\n"
            "Do not modify input variables unless explicitly asked. Compute new values and return updated game state.\n"
            "For example, if the task involves modifying player health or score, always compute the result and return it, "
            "without modifying the original player object unless specified.\n"
            "For game logic, ensure that all necessary conditions (like health > 0) are checked."
        )
    },
    {
        "role": "user",
        "content": f"Here is the code:\n{code_input}\n\nPlease apply the following change:\n{user_prompt}\n\nOnly return the parts of the code you changed."
    }
    ]

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=messages,
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # Extract code block using regex
    code_match = re.search(r"```python(.*?)```", content, re.DOTALL)
    modified_code = code_match.group(1).strip() if code_match else content

    # Extract explanation
    explanation_match = re.search(r"Explanation:(.*)", content, re.DOTALL)
    explanation = explanation_match.group(1).strip() if explanation_match else "No explanation provided."

    return modified_code, explanation

    content = response.choices[0].message.content.strip()

    if "Explanation:" in content:
        modified_code, explanation = content.split("Explanation:", 1)
    else:
        modified_code, explanation = content, "No explanation provided."

    return modified_code.strip(), explanation.strip()
