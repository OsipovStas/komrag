import sys
import os
from dotenv import load_dotenv
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(".env", override=True)

# Import and run your actual Streamlit app
from ui import chat

chat.main()