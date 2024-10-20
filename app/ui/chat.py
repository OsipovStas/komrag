from rag.rag_chain import create_rag_chain, create_rag_chain_colab  # Replace with your actual import
import streamlit as st
import os
from dotenv import load_dotenv



@st.cache_resource
def get_rag_chain():
    if os.environ["IS_COLAB"]:
        return create_rag_chain_colab()
    else:
        return create_rag_chain()


def main():
    # Initialize your RAG chain
    rag_chain = get_rag_chain()

    st.title("Komrag Bot")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input:
            # Append user message
            st.session_state['messages'].append(("User", user_input))

            # Get response from RAG chain
            response = rag_chain.invoke(user_input)

            # Append bot response
            st.session_state['messages'].append(("Bot", response))

    # Display chat history
    for sender, message in st.session_state['messages']:
        st.write(f"{sender}: {message}")


if __name__ == "__main__":
    load_dotenv(".env", override=True)
    main()
