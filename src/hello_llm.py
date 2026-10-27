"""hello_llm.py — Your first OpenAI API call.

Run it from the repo root:
python src/hello_llm.py "What is RAG in one sentence?"
"""
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load OPENAI_API_KEY from .env if a .env file exists.
# On Vocareum the key is already set in the environment, so this is a
# harmless no-op.
load_dotenv()
# Create the OpenAI client — it reads OPENAI_API_KEY from the
# environment automatically.
client = OpenAI()

def main() -> None:
    # Use the question from the command line, or a default one.
    question = " ".join(sys.argv[1:]) or "What is RAG in one sentence?"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
