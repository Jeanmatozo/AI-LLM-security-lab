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
    # If overridden by user input, the model may hallucinate or misbehave.
    system_message = (
        "You are a helpful cybersecurity assistant. "
        "You answer in short, clear sentences and avoid hallucinating."
    )

    while True:
        # UNTRUSTED USER INPUT
        # This is a primary trust boundary: external input enters the system here.
        user_input = input("You: ")

        if user_input.strip().lower() in ("exit", "quit"):
            print("Chatbot: Goodbye!")
            break

        # TRUST BOUNDARY:
        # System instructions (trusted) and user input (untrusted)
        # are combined into a single prompt sent to the LLM.
