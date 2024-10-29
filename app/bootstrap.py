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

# Import and run your actual Streamlit app
from ui import chat

chat.main()