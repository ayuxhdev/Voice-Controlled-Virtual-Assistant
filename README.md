# Jarvis - Voice-Controlled Virtual Assistant

## Project Overview

Jarvis is a Python-based voice-controlled virtual assistant that listens for the wake word **"Jarvis"**, understands spoken commands, and responds through text-to-speech.

The project currently supports basic voice commands such as opening websites, playing songs, fetching news headlines, and answering general questions using the OpenAI API.

## Features

* Wake-word activation using **SpeechRecognition**
* Converts speech into text using **Google Speech Recognition**
* Text-to-speech responses using **gTTS** and **pygame**
* Offline text-to-speech support using **pyttsx3**
* Opens websites such as Google, YouTube, Instagram, Facebook, and LinkedIn
* Plays songs from a local music library
* Uses `difflib` for approximate song-name matching
* Fetches the latest news headlines using **NewsAPI**
* Uses the **OpenAI API** for general questions

## Tech Stack

* Python
* SpeechRecognition
* PyAudio
* gTTS
* pyttsx3
* pygame
* Requests
* OpenAI API
* NewsAPI
* difflib

## How It Works

1. The assistant continuously listens for the wake word **"Jarvis"**.
2. Once the wake word is detected, it listens for the user's command.
3. The spoken command is converted into text.
4. The command is checked against the available functions:

   * Open a website
   * Play a song
   * Fetch news
   * Process a general question using OpenAI
5. The response is then spoken back to the user.

## Project Structure

```text
Jarvis/
│
├── main.py
├── client.py
├── musicLibrary.py
├── newsapikey.txt
├── Requirements.txt
└── README.md
```

### File Description

* `main.py` - Main program containing the voice assistant logic and command processing.
* `client.py` - Separate OpenAI API example/test file.
* `musicLibrary.py` - Contains the music names and their corresponding YouTube links.
* `newsapikey.txt` - Stores the NewsAPI key used by the project.
* `Requirements.txt` - Contains the Python dependencies required for the project.
* `README.md` - Project documentation.

## Example Commands

The assistant can respond to commands such as:

```text
"Jarvis, open Google"
"Jarvis, open YouTube"
"Jarvis, play Despacito"
"Jarvis, give me the latest news"
```

For other questions, the assistant can use the OpenAI API to generate a response.

## Current Limitations

* The command system is currently based on predefined conditions.
* The assistant requires an internet connection for Google Speech Recognition, gTTS, NewsAPI, and OpenAI features.
* The current OpenAI integration is still basic.
* The wake-word detection relies on speech recognition rather than a dedicated wake-word engine.
* API keys are currently handled separately and will be improved in a future version.

## Future Improvements

* Secure API key management using environment variables.
* Improve the OpenAI integration to process the user's actual voice commands.
* Build a more flexible command/plugin system.
* Add more useful voice commands.
* Add a graphical user interface.
* Improve wake-word detection.
* Make the assistant more conversational and context-aware.

## Project Status

**Version 1 - Basic Voice Assistant**

The initial version of the project is functional and provides the foundation for future improvements.
