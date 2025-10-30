import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="My Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 My Chatbot")

# --- Inject CSS for alignment ---
st.markdown(
    """
    <style>
    .chat-message {
        padding: 8px 12px;
        margin: 6px 0;
        border-radius: 10px;
        max-width: 70%;
    }
    .chat-user {
        background-color: #DCF8C6;  /* WhatsApp-style green */
        margin-left: auto;
        text-align: right;
    }
    .chat-bot {
        background-color: #F1F0F0;  /* light gray */
        margin-right: auto;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory" not in st.session_state:
    st.session_state.memory = InMemoryChatMessageHistory()


# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Controls")

    # Reset Session
    if st.button("🔄 New Session"):
        st.session_state.chat_history = []
        st.session_state.memory = InMemoryChatMessageHistory()
        st.success("Session reset!")

    # User settable parameters
    temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
    max_tokens = st.number_input(
        "Max Tokens", min_value=100, max_value=4096, value=1024, step=100
    )


# --- Initialize LLM ---
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0.7,
    reasoning_format="hidden",  # hide reasoning traces
)

# --- Chat Input (fixed at bottom) ---
user_input = st.chat_input("Type your message...")

if user_input:
    try:
        # Add user message
        st.session_state.memory.add_user_message(user_input)
        st.session_state.chat_history.append(("user", user_input))

        # Prepare full context
        all_messages = st.session_state.memory.messages
        prompt_text = "\n".join(
            f"You: {m.content}" if isinstance(m, HumanMessage) else f"Bot: {m.content}"
            for m in all_messages
        )

        # Get response from LLM
        llm_response = llm.invoke(prompt_text)

        # Save AI response
        st.session_state.memory.add_ai_message(llm_response.content)
        st.session_state.chat_history.append(("bot", llm_response.content))

    except Exception as e:
        st.error(f"Error: {str(e)}")

# --- Display Chat History ---
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(
            f'<div class="chat-message chat-user">{msg}</div>', unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-message chat-bot">{msg}</div>', unsafe_allow_html=True
        )


# how to run it
# type in terminal- streamlit run filename.py
