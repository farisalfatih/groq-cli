import sys
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("GROQ_API_KEY not found")
        return

    if len(sys.argv) < 2:
        print('usage: groq "prompt"')
        return

    prompt = sys.argv[1]

    client = Groq(api_key=api_key)

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(res.choices[0].message.content)


if __name__ == "__main__":
    main()
