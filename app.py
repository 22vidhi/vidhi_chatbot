import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
import base64
import ollama


import ollama

def get_ollama_response(prompt):
    response = ollama.chat(
        model="llama2",   # or any model you pulled (e.g., "mistral", "codellama", etc.)
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]

# -------------------- MODERN CHAT UI --------------------


# -------------------- UNIFIED BACKGROUND STYLE --------------------

highlight_theme = """
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background: #ffffff;  /* White background */
    color: #000000;       /* Black text */
    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    
    background: #000000;  /* black sidebar */
    color: #ffffff; /* white text */
}

/* Chat messages */
.stChatMessage {
    padding: 12px;
    border-radius: 15px;
    margin: 8px 0;
    font-size: 16px;
}

/* User messages */
.stChatMessage.user {
    background: ##0077b6;  /* Light black for user */
    color: #ffffff; /* White text */
    border-radius: 15px 15px 0px 15px;
    box-shadow: 0px 0px 10px #a0d8ff; /* Glow highlight */
    font-weight: 500;
}

/* Bot messages (highlighted) */
.stChatMessage.assistant {
    background: ##0077b6;  /* Light black for user */
    color: #ffffff; /* White text */
    border-radius: 15px 15px 0px 15px;
    box-shadow: 0px 0px 10px #a0d8ff; /* Glow highlight */
    font-weight: 500;
}

/* Input box */
textarea, input {
    background: #ffffff !important;  /* White input */
    color: #000000 !important;       /* Black text */
    border-radius: 12px !important;
    border: 1px solid #ccc !important;
}
textarea::placeholder, input::placeholder {
    color: #888 !important;
}

/* Buttons - solid white */
div.stButton > button {
    background: #ffffff;
    color:#000000;
    border-radius: 12px;
    border: 1px solid #aaa;
    padding: 8px 16px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
}
div.stButton > button:hover {
    background: #f0f0f0;
    border: 1px solid #888;
}

/* Footer */
footer, .stFooter {
    background: #ffffff !important;
    color: #555 !important;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
}
</style>
"""

# Sidebar header with black background
st.sidebar.markdown("""
<div style="
    background-color: #000000;
    color: #ffffff;
    padding: 12px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
">
⚙️ Settings
</div>
""", unsafe_allow_html=True)

# Mode selection container
st.sidebar.markdown("""
<div style="
    background-color: #111111;
    color: #ffffff;
    padding: 12px;
    border-radius: 10px;
    margin-top: 10px;
    font-family: 'Segoe UI', sans-serif;
">
<b>Select Mode</b>
</div>
""", unsafe_allow_html=True)

# Radio buttons with custom styling
mode = st.sidebar.radio(
    "",
    ["💬 Text → Text", "🗣️ Text → Voice", "🎤 Voice → Voice"],
    index=0,
    key="mode_selector"
)

# Highlight the selected mode with a black background and white text
st.sidebar.markdown(f"""
<div style="
    background-color: #000000;
    color: #ffffff;
    padding: 8px 12px;
    border-radius: 8px;
    margin-top: 5px;
    font-family: 'Segoe UI', sans-serif;
    font-weight: 500;
">
Current Mode: {mode}
</div>
""", unsafe_allow_html=True)


# Apply CSS
st.markdown(highlight_theme, unsafe_allow_html=True)

# Footer text
st.markdown("<footer>⚡ Chatbot © 2025</footer>", unsafe_allow_html=True)

# -------------------- APP TITLE --------------------
st.markdown("""
<div style="text-align: center; margin-top: -30px;">
    <h1>🤖 Vidhi's Chatbot</h1>
    <p>Your AI-powered assistant for text & voice conversations</p>
</div>
""", unsafe_allow_html=True)




# # -------------------- MAIN TITLE --------------------
# st.title("🤖 Vidhi's Chatbot")
# st.caption("Your AI-powered assistant for text & voice conversations")


# -------------------- SIDEBAR --------------------
#st.sidebar.title("⚙️ Settings")

#mode = st.sidebar.radio("Select Mode", ["💬 Text → Text", "🗣️ Text → Voice", "🎤 Voice → Voice"])

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []

if st.sidebar.button("📄 Export Chat"):
    chat_export = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
    b64 = base64.b64encode(chat_export.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="chat.txt">⬇️ Download Chat</a>'
    st.sidebar.markdown(f'<div class="download-chat">{href}</div>', unsafe_allow_html=True)

# -------------------- Text-to-Speech --------------------
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# -------------------- Speech-to-Text --------------------
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.success(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio")
    except sr.RequestError:
        st.error("⚠️ API unavailable")
    return None

# -------------------- Typing Effect --------------------
def typing_effect(container, text):
    message_placeholder = container.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        message_placeholder.markdown(typed_text)
        time.sleep(0.02)

# -------------------- Session State --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []



# # --- Sidebar UI ---
# st.sidebar.title("⚙️ Settings")

# mode = st.sidebar.radio("Select Mode", ["💬 Text → Text", "🗣️ Text → Voice", "🎤 Voice → Voice"])

# if st.sidebar.button("🗑️ Clear Chat"):
#     st.session_state.messages = []

# if st.sidebar.button("📄 Export Chat"):
#     chat_export = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
#     b64 = base64.b64encode(chat_export.encode()).decode()
#     href = f'<a href="data:file/txt;base64,{b64}" download="chat.txt">⬇️ Download Chat</a>'
#     st.sidebar.markdown(f'<div class="download-chat">{href}</div>', unsafe_allow_html=True)

# -------------------- Header --------------------
# st.markdown("""
# <h1 style='text-align: center; 
#            background: -webkit-linear-gradient(#1E88E5, #1565C0);
#            -webkit-background-clip: text;
#            -webkit-text-fill-color: transparent;
#            font-size: 42px;'>
# 🤖 Vidhi's Smart Chatbot
# </h1>
# <p style='text-align: center; color: #666; font-size:18px;'>
# Your AI-powered assistant for text & voice conversations
# </p>
# """, unsafe_allow_html=True)


# -------------------- Custom CSS --------------------
st.markdown("""
<style>
/* App dark background */
.stApp {
    background: linear-gradient(-45deg, #141E30, #243B55, #1f1c2c, #16222A);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Chat bubbles */
.user-bubble {
    background-color: #2D3748;  /* Dark gray-blue */
    color: #E2E8F0;             /* Light text */
    padding: 10px 15px;
    border-radius: 18px 18px 0px 18px;
    max-width: 75%;
    margin: 8px 0;
    align-self: flex-end;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
}

.bot-bubble {
    background-color: #1A365D;  /* Deep dark blue */
    color: #E2E8F0;
    padding: 10px 15px;
    border-radius: 18px 18px 18px 0px;
    max-width: 75%;
    margin: 8px 0;
    align-self: flex-start;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)




# -------------------- Chat UI --------------------
user_input = None
if mode == "💬 Text → Text" or mode == "🗣️ Text → Voice":
    user_input = st.chat_input("Type your message...")
elif mode == "🎤 Voice → Voice":
    if st.button("🎤 Speak Now"):
        spoken_text = speech_to_text()
        if spoken_text:
            user_input = spoken_text
            
# -------------------- Process Input --------------------
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Ollama response
    response = get_ollama_response(user_input)

    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Speak response if needed
    if mode in ["🗣️ Text → Voice", "🎤 Voice → Voice"]:
        speak_text(response)

# -------------------- Display Chat History --------------------
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        with st.chat_message("user", avatar="🪶"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            if i == len(st.session_state.messages) - 1:
                # ✅ Typing effect only for latest assistant message
                placeholder = st.empty()
                typing_effect(placeholder, msg["content"])
            else:
                st.markdown(msg["content"])






# -------------------- Display Chat History --------------------
# #*

# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         with st.chat_message("user", avatar="👤"):
#             st.markdown(msg["content"])
#     else:
#         with st.chat_message("assistant", avatar="🤖"):
#             st.markdown(msg["content"])
            
