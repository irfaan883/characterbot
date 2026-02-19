import streamlit as st
import ollama

# Page config
st.set_page_config(page_title="Luffy AI", page_icon="🏴‍☠️", layout="centered")

# ---- Premium UI CSS ----
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    background-attachment: fixed;
}

/* Header */
.header {
    text-align: center;
    color: white;
    margin-bottom: 15px;
}

.header h1 {
    font-size: 40px;
    margin-bottom: 0;
}

.header p {
    color: #facc15;
    font-size: 16px;
}

/* Chat container */
.chat-container {
    max-width: 700px;
    margin: auto;
}

/* User message */
.user-msg {
    background: rgba(0,0,0,0.7);
    color: white;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    text-align: right;
    backdrop-filter: blur(6px);
}

/* Luffy message */
.bot-msg {
    background: linear-gradient(90deg, #ff512f, #f09819);
    color: white;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

/* Avatar */
.avatar {
    font-size: 20px;
    margin-right: 6px;
}

/* Input styling */
.stChatInput input {
    border-radius: 12px;
    border: none;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown("""
<div class="header">
    <h1>🏴‍☠️ Monkey D. Luffy</h1>
    <p>Future King of the Pirates • Let's go on an adventure!</p>
</div>
""", unsafe_allow_html=True)

# ---- Luffy Personality ----
character_prompt = """
You are Monkey D. Luffy from One Piece.

Personality:
- Energetic, cheerful, fearless
- Short, exciting replies
- Talk about adventure, dreams, friendship
- Sometimes say: "Shishishi!", "I'm gonna be King of the Pirates!"
- Simple, fun language
- Stay fully in character
"""

# ---- Session Memory ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": character_prompt}
    ]

# ---- Chat Display ----
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-msg"><b>You:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-msg"><span class="avatar">🏴‍☠️</span><b>Luffy:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# ---- Input ----
user_input = st.chat_input("Talk to Luffy...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Typing indicator
    with st.spinner("Luffy is thinking..."):
        response = ollama.chat(
            model="gemma3:1b",
            messages=st.session_state.messages
        )

    reply = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()