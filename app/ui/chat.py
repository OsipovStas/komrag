from langfuse import Langfuse

from rag.rag_chain import create_rag_chain, create_rag_chain_colab
import streamlit as st
import os
from dotenv import load_dotenv

from utils.langfuse import langfuse_handler
from langfuse.decorators import observe
from langfuse.decorators import langfuse_context

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

@st.cache_resource
def get_langfuse_client():
    config = st.secrets.langfuse
    if not config.enabled:
        return None
    return Langfuse(
        secret_key=st.secrets.langfuse.sk,
        public_key=st.secrets.langfuse.pk,
        host=st.secrets.langfuse.host,)


def score_trace(num, value):
    lf = get_langfuse_client()
    if lf:
        lf.score(
            trace_id=st.session_state["traces"][num],
            name="user-explicit-feedback",
            value=value,
        )
    pass


def main():
    st.title("Komrag Bot")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
        st.session_state['traces'] = []
        st.session_state['feedback'] = {}

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input:
            # Append user message
            st.session_state['messages'].append(("User", user_input))

            # Get response from RAG chain
            response, trace_id = invoke_bot(user_input)

            # Append bot response
            st.session_state['messages'].append(("Bot", response))

            st.session_state["traces"].append(trace_id)


    # Display chat history with feedback buttons
    for i, (sender, message) in enumerate(st.session_state['messages']):
        st.write(f"{sender}: {message}")
        if sender == "Bot":
            # Track feedback to mark the most recent/relevant one as active
            feedback = st.session_state['feedback'].get(i, None)
            style_up = "primary" if feedback == 'up' else "secondary"
            style_down = "primary" if feedback == 'down' else "secondary"

            col1, col2, spacer = st.columns([0.1, 0.1, 0.8])
            with col1:
                if st.button('👍', key=f"up_{i}", help="Thumbs Up", type=style_up):
                    st.session_state['feedback'][i] = 'up'
                    score_trace(num=i // 2 , value=1)
                    st.rerun()
            with col2:
                if st.button('👎', key=f"down_{i}", help="Thumbs Down", type=style_down):
                    st.session_state['feedback'][i] = 'down'
                    score_trace(num=i // 2, value=0)
                    st.rerun()


@observe
def invoke_bot(user_input):
    handler = langfuse_context.get_current_langchain_handler()
    trace_id = langfuse_context.get_current_trace_id()
    response = get_rag_chain().invoke(user_input, {"callbacks": [handler]})
    return response, trace_id


if __name__ == "__main__":
    load_dotenv(".env", override=True)
    main()