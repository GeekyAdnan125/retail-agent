import streamlit as st
from agent import recomend_product

# Page config
st.set_page_config(
    page_title="Retail Product Chatbot",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Retail Product ChatBot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = None

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("How can I assist you today?")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    response = recomend_product(user_input)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(response)