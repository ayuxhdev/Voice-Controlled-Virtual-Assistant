# Sonic - Voice-Controlled Virtual Assistant

## Project Overview

Sonic is a Python-based voice-controlled virtual assistant that listens for the wake word **"Sonic"**, understands spoken commands, and responds through text-to-speech.

Sonic supports common voice commands such as opening websites, playing music from YouTube, fetching news headlines, and answering general questions using the **Gemini API**.

The project is organized into separate modules for voice processing, AI interaction, command handling, web operations, and media playback, making it easier to maintain and extend.

## Features

* Wake-word activation using **SpeechRecognition**
* Converts speech into text using **Google Speech Recognition**
* Remains active and listens for multiple commands after the wake word is detected
* Returns to wake-word mode when the user says **"stop listening"**
* Text-to-speech responses using **gTTS** and **pygame**
* Offline text-to-speech support using **pyttsx3**
* Opens websites such as Google, YouTube, Instagram, Facebook, and LinkedIn
* Searches YouTube for requested songs using **yt-dlp**
* Downloads the selected audio temporarily for playback
* Plays downloaded audio using **VLC**
* Automatically deletes downloaded audio files after playback finishes
* Fetches the latest news headlines using **NewsAPI**
* Uses the **Gemini API** for general questions
* Uses a modular project structure for easier development and future upgrades

## Tech Stack

* Python
* SpeechRecognition
* PyAudio
* gTTS
* pyttsx3
* pygame
* Requests
* yt-dlp
* python-vlc
* VLC Media Player
* Gemini API
* NewsAPI
* difflib
* python-dotenv

## How It Works

1. Sonic continuously listens for the wake word **"Sonic"**.
2. Once the wake word is detected, Sonic becomes active.
3. Sonic listens for commands continuously without requiring the wake word again.
4. The spoken command is converted into text using Google Speech Recognition.
5. The command is sent to the command-processing module.
6. The command is checked against the available functions:

   * Open a website
   * Play music
   * Fetch news
   * Process a general question using Gemini
7. For music playback, Sonic searches YouTube using **yt-dlp**.
8. The selected audio is downloaded temporarily into `music_cache`.
9. VLC plays the downloaded audio file.
10. After playback finishes, Sonic releases the VLC player and removes the temporary audio file.
11. Sonic remains active until the user says **"stop listening"**.
12. After that, Sonic returns to wake-word mode.

## Project Structure

```text
Voice-Controlled-Virtual-Assistant/

│
├── .gitignore
├── .env
├── main.py
├── voice.py
├── ai.py
├── commands.py
├── web_search.py
├── musicLibrary.py
├── Requirements.txt
└── README.md
```

> `music_cache/` is created automatically when Sonic downloads audio. It is a runtime folder and should be excluded from Git tracking.

> `.env` contains local API keys and is excluded from Git tracking using `.gitignore`.

### File Description

* `main.py` - Controls the overall application flow, wake-word detection, and interaction between the different modules.
* `voice.py` - Handles speech recognition and text-to-speech functionality.
* `ai.py` - Handles Gemini API communication and AI-generated responses.
* `commands.py` - Handles command processing, including websites, music, news, and routing general questions to Gemini.
* `web_search.py` - Handles web searching, YouTube result extraction, audio downloading, and VLC-based audio playback.
* `musicLibrary.py` - Contains the project's existing music-related data and links.
* `Requirements.txt` - Contains the Python dependencies required for the project.
* `.env` - Stores API keys and local configuration. This file is not committed to the repository.
* `.gitignore` - Specifies files and folders that Git should ignore.
* `README.md` - Project documentation.

## Example Commands

The assistant can respond to commands such as:

```text
"Sonic, open Google"

"Sonic, open YouTube"

"Sonic, play Meant for You"

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

* The command system still relies largely on predefined conditions.
* Sonic requires an internet connection for Google Speech Recognition, NewsAPI, Gemini, and YouTube-based music playback.
* Wake-word detection relies on general speech recognition rather than a dedicated wake-word engine.
* Speech recognition may occasionally misunderstand commands depending on microphone quality, background noise, or pronunciation.
* Sonic currently does not maintain conversation history between questions.
* AI responses are generated independently for each general question.
* While music is playing, Sonic continues listening for commands. Music can sometimes be interpreted as speech, which may result in repeated messages such as **"Sorry, I didn't understand that."**
* YouTube extraction depends on third-party `yt-dlp` behavior and available formats.
* VLC Media Player must be installed separately because `python-vlc` is a Python interface to VLC rather than the media player itself.

## Future Improvements

* Improve handling of music playback and command listening
* Add conversation memory and context awareness
* Improve handling of longer and more natural questions
* Make Gemini responses more conversational and optimized for voice
* Build a more flexible command and plugin system
* Add general YouTube video playback
* Add pause, resume, stop, and volume controls
* Improve wake-word detection
* Improve overall error handling and application structure
* Add a graphical user interface

## Project Status

**Version 2 - Voice Assistant with YouTube Music Playback**

Sonic V2 currently includes:

* Wake-word activation
* Continuous command listening
* Website automation
* YouTube music search
* Audio downloading using `yt-dlp`
* Audio playback using VLC
* Automatic cleanup of downloaded audio
* NewsAPI integration
* Gemini integration
* Modular project structure
* Environment-based API key management

The project is actively being developed. The next major development phase will focus on making Sonic more intelligent and context-aware while expanding its GenAI capabilities.
