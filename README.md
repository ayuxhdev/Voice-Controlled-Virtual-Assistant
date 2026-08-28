# Sonic - Voice-Controlled Virtual Assistant

## Project Overview

Sonic is a Python-based voice-controlled virtual assistant that listens for the wake word **"Sonic"**, understands spoken commands, and responds through text-to-speech.

The project currently supports basic voice commands such as opening websites, playing songs, fetching news headlines, and answering general questions using the **Gemini API**.

## Features

* Wake-word activation using **SpeechRecognition**
* Converts speech into text using **Google Speech Recognition**
* Remains active and listens for multiple commands after the wake word is detected
* Returns to wake-word mode when the user says **"stop listening"**
* Text-to-speech responses using **gTTS** and **pygame**
* Offline text-to-speech support using **pyttsx3**
* Opens websites such as Google, YouTube, Instagram, Facebook, and LinkedIn
* Plays songs from a local music library
* Uses `difflib` for approximate song-name matching
* Fetches the latest news headlines using **NewsAPI**
* Uses the **Gemini API** for general questions

## Tech Stack

* Python
* SpeechRecognition
* PyAudio
* gTTS
* pyttsx3
* pygame
* Requests
* Gemini API
* NewsAPI
* difflib
* python-dotenv

## How It Works

1. Sonic continuously listens for the wake word **"Sonic"**.
2. Once the wake word is detected, Sonic becomes active.
3. Sonic listens for user commands continuously.
4. The spoken command is converted into text using Google Speech Recognition.
5. The command is checked against the available functions:

   * Open a website
   * Play a song
   * Fetch news
   * Process a general question using Gemini
6. The response is converted into speech and played back.
7. Sonic remains active until the user says **"stop listening"**.

## Project Structure

```text
Voice-Controlled-Virtual-Assistant/
│
├── .gitignore
├── .env
├── main.py
├── musicLibrary.py
├── Requirements.txt
└── README.md
```

> `.env` contains local API keys and is excluded from Git tracking using `.gitignore`.

### File Description

* `main.py` - Main program containing the voice assistant logic, command processing, Gemini integration, and speech handling.
* `musicLibrary.py` - Contains song names and their corresponding YouTube links.
* `Requirements.txt` - Contains the Python dependencies required for the project.
* `.env` - Stores API keys and local configuration. This file is not committed to the repository.
* `.gitignore` - Specifies files and folders that Git should ignore.
* `README.md` - Project documentation.

## Example Commands

The assistant can respond to commands such as:

```text
"Sonic, open Google"
"Sonic, open YouTube"
"Sonic, play Despacito"
"Sonic, give me the latest news"
"What is Python?"
```

Once Sonic is activated, multiple commands can be given without repeating the wake word.

To return Sonic to wake-word mode:

```text
"Stop listening"
```

For general questions, Sonic uses the Gemini API to generate a response.

## Current Limitations

* The command system is currently based on predefined conditions.
* The assistant requires an internet connection for Google Speech Recognition, gTTS, NewsAPI, and Gemini features.
* Wake-word detection relies on general speech recognition rather than a dedicated wake-word engine.
* Speech recognition may occasionally misunderstand commands depending on microphone quality, background noise, or pronunciation.
* The current conversational capabilities are basic and do not yet maintain conversation history.

## Future Improvements

* Improve handling of longer and more natural questions.
* Make Gemini responses more conversational and optimized for voice.
* Build a more flexible command/plugin system.
* Add more useful voice commands.
* Add conversation memory and context awareness.
* Improve wake-word detection.
* Add a graphical user interface.
* Improve overall error handling and application structure.

## Project Status

**Version 1 - Basic Voice Assistant**

The initial version of Sonic is functional and provides the foundation for future improvements.

The current version includes Gemini integration, continuous command listening, website automation, music playback, and NewsAPI integration.
