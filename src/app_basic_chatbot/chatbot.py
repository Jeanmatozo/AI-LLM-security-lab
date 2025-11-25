import os
from openai import OpenAI

# Read your API key from an environment variable
# Set it locally as: export OPENAI_API_KEY="your_key_here"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_chat():
    print("Simple LLM Chatbot (type 'exit' to quit)\n")
    system_message = (
        "You are a helpful cybersecurity assistant. "
        "You answer in short, clear sentences and avoid hallucinating."
    )

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("Chatbot: Goodbye!")
            break

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        print(f"Chatbot: {answer}\n")

if __name__ == "__main__":
    simple_chat()
