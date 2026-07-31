# Jarvis — Voice-Controlled Virtual Assistant

A Python-based voice assistant that listens for the wake word "Jarvis," understands spoken commands, and responds using text-to-speech — capable of opening websites, playing music, fetching news, and answering general questions via OpenAI.

## Features
- Wake-word activation ("Jarvis") using `SpeechRecognition`
- Text-to-speech responses via `gTTS` + `pygame` (with `pyttsx3` as an offline fallback)
- Opens websites on command (Google, YouTube, Instagram, Facebook, LinkedIn)
- Plays songs from a local music library, with fuzzy matching (`difflib`) for close song-name matches
- Fetches the latest news headlines via NewsAPI
- Falls back to the OpenAI API for general conversational queries

## Tech Stack
- Python
- SpeechRecognition + PyAudio
- gTTS / pyttsx3 / pygame
- OpenAI API
- NewsAPI
- difflib
- python-dotenv

## How It Works
1. The assistant continuously listens for the wake word "Jarvis".
2. Once activated, it listens for a command and converts speech to text.
3. Based on the command, it either:
   - opens a website,
   - plays a matched song,
   - fetches news headlines, or
   - sends the query to the OpenAI API for a natural language response.
4. The response is converted to speech and played back.

## Project Structure
```
├── main.py            # Core assistant logic
├── musicLibrary.py     # Song name → link mapping
├── requirements.txt    # Python dependencies
└── .env.example        # Template for required environment variables
```

## Future Improvements
- Custom wake-word detection without relying on the general speech recognizer
- Expandable command/plugin system
- GUI interface

## License
This project is open source under the [MIT License](LICENSE).