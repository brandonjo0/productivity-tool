from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiClient:
    """
    A client wrapper for interacting with the Gemini API.

    Loads the API key from the .env file and provides a simple interface for generating model responses.
    """
    def __init__(self):
        """
        Constructs a new GeminiClient.

        Initializes the client using the API key loaded from the .env file and sets the model name.
        """
        self.client = genai.Client(api_key=os.getenv("API_KEY"))
        self.model_name = "gemini-2.5-pro"

    def request(self, prompt):
        """
        Sends a prompt to the Gemini model and returns the generated text.

        @param prompt: The text prompt to send to the model.
        @return: The generated response text from the model.
        """
        response = self.client.models.generate_content(
            model = self.model_name,
            contents = prompt
        )
        return response.text
