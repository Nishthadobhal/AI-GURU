import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt: str):

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except ServerError as e:
        print("SERVER ERROR:", e)
        return "Gemini server is busy right now. Please try again in a few moments."

    except Exception as e:
        print("OTHER ERROR:", type(e))
        print(e)
        raise