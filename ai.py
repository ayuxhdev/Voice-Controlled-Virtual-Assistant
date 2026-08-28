from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

def aiProcess(c) :
    client = genai.Client(
        api_key = os.getenv("GEMINI_API_KEY")
    )
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents = c,
        config = types.GenerateContentConfig(
            system_instruction = (
                "Your name is Sonic. "
                "You are a helpful voice assistant. "
                "Answer questions naturally and clearly. "
                "Keep simple questions concise, but provide more detail "
                "when the question requires it. "
                "Use natural spoken language rather than markdown "
                "or unnecessary formatting. "
                "Your responses will be spoken aloud. "
            )
        )
    )
    
    return response.text