import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError, ClientError

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

    except ServerError:
        return "Gemini server is busy right now. Please try again in a few moments."

    except ClientError as e:
        return f"Gemini API Error: {e}"

    except Exception as e:
        return f"Unexpected Error: {e}"