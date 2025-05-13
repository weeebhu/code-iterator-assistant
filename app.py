import streamlit as st
from code_modifier import modify_code
from code_integrator import integrate_code, get_code_diff

st.set_page_config(page_title="Aicade Code Iterator AI", layout="wide")
st.title("🎮 Aicade Code Iterator")

st.markdown("""
Use this AI assistant to edit or improve selected game code based on natural language instructions.
""")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "final_code" not in st.session_state:
    st.session_state.final_code = None

if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None

code_input = st.text_area("📝 Paste your code here", height=250)
user_prompt = st.text_input("💡 What would you like to change or improve in the code?")

if st.button("✨ Generate Suggestion"):
    if code_input and user_prompt:
        with st.spinner("Thinking..."):
            try:
                modified_snippet, explanation = modify_code(code_input, user_prompt)
                code_diff = get_code_diff(code_input, modified_snippet)

                st.subheader("✅ Suggested Snippet")
                st.code(modified_snippet, language="python")

                st.subheader("🔍 Explanation")
                st.write(explanation)

                st.subheader("📋 Diff View (Against Full Code)")
                st.code(code_diff, language="diff")

                st.session_state.chat_history.append({
                    "prompt": user_prompt,
                    "original_code": code_input,
                    "modified_snippet": modified_snippet,
                    "explanation": explanation,
                    "diff": code_diff
                })
                st.session_state.last_prompt = user_prompt
                st.session_state.last_code = code_input
                st.session_state.final_code = None

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter both code and a prompt to continue.")

if st.session_state.chat_history:
    st.subheader("🧠 Previous Interactions")
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        with st.expander(f"Prompt: {chat['prompt']}"):
            st.markdown("**🔁 Modified Snippet**")
            st.code(chat['modified_snippet'], language="python")

            st.markdown("**📋 Diff View**")
            st.code(chat['diff'], language="diff")

            st.markdown("**🧠 Explanation**")
            st.write(chat['explanation'])

            if st.button("🧩 Integrate This Code", key=f"integrate_{i}"):
                try:
                    integrated = integrate_code(chat['original_code'], chat['modified_snippet'])
                    st.session_state.final_code = integrated
                except Exception as e:
                    st.error(f"❌ Integration Error: {str(e)}")

if st.session_state.final_code:
    st.subheader("✅ Final Integrated Code")
    st.code(st.session_state.final_code, language="python")
