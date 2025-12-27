# src/app_basic_chatbot/chatbot.py

import os
from openai import OpenAI

# Read API key from environment variable
# NOTE: Secrets should never be hardcoded
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple_chat():
    """
    Simple chatbot demonstrating direct user-to-LLM interaction.

    SECURITY NOTE:
    - User input is untrusted
    - System message defines intended behavior and safety constraints
    """
    print("Simple LLM Chatbot (type 'exit' to quit)\n")

    # TRUSTED SYSTEM INSTRUCTIONS
    # This message defines desired behavior and safety posture.
    # If overridden by user in

