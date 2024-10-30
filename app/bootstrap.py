import sys
import os
from dotenv import load_dotenv
import streamlit as st
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(".env", override=True)
# Iterate through all secrets and set them as environment variables
for key, value in st.secrets.items():
    os.environ[key] = str(value)

from langfuse.decorators import langfuse_context

# Configure the Langfuse client
langfuse_context.configure(
    secret_key=st.secrets.langfuse.sk,
    public_key=st.secrets.langfuse.pk,
    host=st.secrets.langfuse.host,
    enabled=st.secrets.langfuse.enabled,
)



# Import and run your actual Streamlit app
from ui import chat

chat.main()