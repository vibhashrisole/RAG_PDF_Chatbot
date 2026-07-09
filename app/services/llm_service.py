import os
from ollama import Client

# OLLAMA CLIENT

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

client = Client(host=OLLAMA_HOST)

# LLM MODEL

MODEL_NAME = "llama3.2"

# GENERATE ANSWER

def generate_answer(question, context):

    prompt = f"""
You are an AI Assistant.

Answer ONLY from the given context.

If the answer is not available in the context, reply exactly:

"I couldn't find the answer in the uploaded PDF."

Do not use your own knowledge.
Do not guess.
Only answer from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error while communicating with Ollama: {str(e)}"