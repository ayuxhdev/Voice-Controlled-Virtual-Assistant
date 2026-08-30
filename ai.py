from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

conversation_history = []

def aiProcess(c) :
    
    global conversation_history 
    
    client = genai.Client(
        api_key = os.getenv("GEMINI_API_KEY")
    )
    
    conversation_history.append(
        {
            "role" : "user",
            "parts" : [{"text" : c}]
        }
    )
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents = conversation_history,
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
    
    conversation_history.append(
        {
            "role" : "model",
            "parts" : [{"text" : response.text}]
        }
    )
    
    return response.text

def clear_conversation() :
    global conversation_history
    conversation_history = []