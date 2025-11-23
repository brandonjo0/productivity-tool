from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("API_KEY"))
        self.model_name = "gemini-2.5-pro"

    def request(self, prompt):
        response = self.client.models.generate_content(
            model = self.model_name,
            contents = prompt
        )
        return response.text
