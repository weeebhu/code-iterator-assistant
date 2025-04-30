import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"],
                base_url=st.secrets["OPENAI_BASE_URL"])

def modify_code(code_input, user_prompt):
    system_prompt = (
            """
            You are a coding assistant for game developers. You receive a code snippet and an instruction.
            You must return:
            1. The improved code snippet.
            2. A brief explanation of what was changed and why.
            """
    )

    messages=[
    {"role": "system", "content": "You are a helpful coding assistant specialized in game development. Modify user code based on instructions and explain the changes clearly."},
    {"role": "user", "content": f"Here is the code:\n{code_input}\n\nPlease apply the following change:\n{user_prompt}\n\nReturn ONLY improved code and explanation separately."}
    ]

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=messages,
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # Split modified code and explanation
    if "Explanation:" in content:
        modified_code, explanation = content.split("Explanation:", 1)
    else:
        modified_code, explanation = content, "No explanation provided."

    return modified_code.strip(), explanation.strip()