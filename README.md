<<<<<<< HEAD
# 🎮 Aicade Code Iterator AI

**Aicade Code Iterator AI** is a developer-friendly tool that uses an AI assistant to help you iteratively improve game-related code. With natural language instructions, you can generate suggestions, view diffs, and integrate improvements directly into your workflow—all within a Streamlit interface.

---

## ✨ Features

- 📝 Paste your code into the editor  
- 💡 Enter a natural language instruction (e.g., "Add gravity to the player movement")  
- 🤖 AI-generated code suggestions using `mistralai/mistral-7b-instruct`  
- 📋 Diff view to compare original vs. modified code  
- 🔍 Clear explanation of changes  
- 🧩 One-click integration of improvements into the original code  
- 🧠 View history of all past interactions  

---

## 🚀 Live Demo

- https://code-iterator-assistant-shc7pvttbpbeblmajujiuv.streamlit.app/

## 📦 Installation

- Clone the repository
     git clone https://github.com/yourusername/aicade-code-iterator.git
     cd aicade-code-iterator

- Install dependencies
    pip install -r requirements.txt

- Setup secrets
    Create a .streamlit/secrets.toml file:
    OPENAI_API_KEY = "your-openrouter-api-key"
    OPENAI_BASE_URL = "https://openrouter.ai/api/v1"  # or your preferred base URL

- Run the app
    streamlit run app.py


## 🧠 How It Works

1. The user pastes code and enters a natural language instruction.
2. The modify_code() function sends this to the Mistral-7B model via OpenRouter.
3. The model returns:
4. A new version of the code
5. A human-readable explanation of the changes
6. A unified diff is computed and displayed.
7. Users can review and choose to integrate the modified code into their base.


## 🗂️ Project Structure

├── app.py                # Streamlit UI  
├── code_modifier.py      # Handles LLM calls and prompt structure  
├── code_integrator.py    # Handles diff and integration logic  
├── requirements.txt      # Python dependencies  
└── .streamlit/           
    └── secrets.toml      # API keys and configuration  



## 🛠️ Todo / Future Work

- ✅ Final code integration (retains original code structure)
- 🌐 Deploy to Streamlit Cloud
- 🧪 Add unit tests for diff & integration logic
- 🧵 Enable inline code commenting
- 💬 Add conversational memory with threading


##🙌 Acknowledgements

- Streamlit
- Mistral AI
- OpenRouter
- Inspired by game developers who want quick iteration cycles with AI.












=======
🎮 Aicade Code Iterator AI
Aicade Code Iterator AI is an AI-powered assistant that helps you improve or modify game development code based on natural language instructions. Built with Streamlit, this tool uses LLMs to generate modified code, explanations, and diffs, and lets you integrate changes seamlessly.

✨ Features
📝 Paste your code into the editor

💡 Enter an instruction (e.g., "Add jump mechanic to player movement")

⚙️ LLM-Powered Code Modification using Mistral-7B via OpenRouter API

🔍 Diff View to visualize changes

🧠 Explanation of what and why changes were made

🧩 One-click Code Integration

🧾 History Panel for past interactions and integration

🚀 Live Demo
>>>>>>> 746a0ab0 (snippet advancements)
