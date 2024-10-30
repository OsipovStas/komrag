from rag.rag_chain import create_rag_chain, create_rag_chain_colab  # Replace with your actual import
import streamlit as st
import os
from dotenv import load_dotenv

from utils.langfuse import langfuse_handler


@st.cache_resource
def get_rag_chain():
    if os.environ["IS_COLAB"]:
        return create_rag_chain_colab(st.secrets)
    else:
        return create_rag_chain()

@st.cache_resource
def get_langfuse_handler(config=st.secrets.langfuse):
    if config.enabled:
        return langfuse_handler(config)
    else:
        return None


def main():
    # Initialize your RAG chain
    rag_chain = get_rag_chain()
    callbacks = []
    if get_langfuse_handler():
        callbacks.append(get_langfuse_handler())

    st.title("Komrag Bot")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input:
            # Append user message
            st.session_state['messages'].append(("User", user_input))

            # Get response from RAG chain
            response = rag_chain.invoke(user_input, {"callbacks": callbacks})

            # Append bot response
            st.session_state['messages'].append(("Bot", response))

    # Display chat history
    for sender, message in st.session_state['messages']:
        st.write(f"{sender}: {message}")


if __name__ == "__main__":
    load_dotenv(".env", override=True)
    main()
