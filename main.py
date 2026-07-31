import speech_recognition as sr
import webbrowser
import pyttsx3                 # Text to speech
import musicLibrary
import difflib
import requests
from openai import OpenAI
from gtts import gTTS
import pygame

import os

recognizer = sr.Recognizer()

engine = pyttsx3.init()

newsapi = "YOUR_NEW_NEWSAPI_KEY_HERE"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    # Generate speech and save it to a temp file
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # AFTER it finishes:
    pygame.mixer.music.stop()
    pygame.mixer.quit()      # Close the mixer fully
    os.remove("temp.mp3")    # Now safely delete the file
    
def aiProcess():
    client = OpenAI(
        api_key="YOUR_NEW_OPENAI_API_KEY_HERE",
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": "What is programming?"}
        ]
    )

    print(completion.choices[0].message.content)


    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening google")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening youtube")
        
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("Opening instagram")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening facebook")
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening linkedin")
        
    elif "play" in c.lower():
        command = c.lower().replace("play", "").strip()
        matches = difflib.get_close_matches(command, musicLibrary.music.keys(), n=1, cutoff=0.5)
        if matches:
            song = matches[0]
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak("Please say the name of the song after 'play'.")
            
    elif "news" in c.lower():
        try:
            speak("Fetching the latest news for you.")
            print("Making request to NewsAPI...")
            r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEW_NEWSAPI_KEY_HERE")

            if r.status_code == 200:
                data = r.json()
                print("Response received from NewsAPI.")

                articles = data.get("articles", [])
                print(f"Found {len(articles)} articles.")

                if articles:
                    for i, article in enumerate(articles[:5]):
                        print(f"News {i+1}: {article['title']}")
                        speak(article["title"])
                else:
                    print("No articles found in the response.")
                    speak("Sorry, I couldn't find any news.")
            else:
                print(f"NewsAPI returned status code {r.status_code}")
                speak("Unable to fetch news at the moment.")

        except Exception as e:
            print("Exception occurred while fetching news:", e)
            speak("Something went wrong while fetching the news.")
                
    else:
        # Let openAI handle the request 
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...... ")
    while True:
        r = sr.Recognizer()
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        print("Recognizing....")

        try: 
            with sr.Microphone() as source:
                print("Listening for the wake word......!")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                # Listen for word 
                with sr.Microphone() as source:
                    print("Jarvis Activated...! Listening for the command")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("You said,",command)
                    
                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))