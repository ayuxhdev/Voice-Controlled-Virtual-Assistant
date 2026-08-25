import speech_recognition as sr
import webbrowser
import pyttsx3                 # Text to speech
import musicLibrary
import difflib
import requests
from google import genai
from google.genai import types
from gtts import gTTS
from dotenv import load_dotenv
import pygame
import os

load_dotenv()

recognizer = sr.Recognizer()

engine = pyttsx3.init()

newsapi = "your_news_api_key"

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
    
def aiProcess(c):
    client = genai.Client(
        api_key="Your_Gemini_Api_Key",
    )
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents = c,
        config = types.GenerateContentConfig(
            system_instruction = ("Your name is Sonic."
                                   "You are a helpful Voice Assistant."
                                   "Your role is to give concise, natural, human-like answers"
                                   "to the questions asked."
                                   "Your responses will be spoken aloud.")
        )
    )
    
    return response.text

def listen_for_command():
    
    try :
        # Listen for word 
        with sr.Microphone() as source:
            
            print("Sonic Activated...! Listening for the command")
            
            r.adjust_for_ambient_noise(
                source,
                duration=1)
            
            audio = r.listen(
                source,
                timeout = 10,
                phrase_time_limit = 5)
                            
                            
            command = r.recognize_google(audio)
            print("You said:",command)
                            
            return command
        
    except sr.UnknownValueError :
                        print("Could not understand the audio")
                        speak("Sorry, I didn't understand that!")
                        return None
                                    
    except sr.WaitTimeoutError :
                print("You didn't say anything.")
                speak("You didn't say anything")
                return None
                                
    except Exception as e:
                print("Error:",type(e).__name__,e)
                return None

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
        matches = difflib.get_close_matches(
            command,
            musicLibrary.music.keys(),
            n=1,
            cutoff=0.5
            )
        
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
            r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=your_news_api_key")

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
        # Let Gemini handle the request 
        output = aiProcess(c)
        speak(output)
        
if __name__ == "__main__":
    
    speak("Initializing Sonic...... ")
    
    while True:
        
        r = sr.Recognizer()
        
        # Listen for the wake word "Echo"
        # Obtain audio from the microphone
        
        print("Recognizing....")

        try: 
            with sr.Microphone() as source:
                
                print("Listening for the wake word......!")
                
                r.adjust_for_ambient_noise(
                    source,
                    duration=1
                    )
                
                audio = r.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=5
                    )
                
            word = r.recognize_google(audio)
            
            print("Recognized",word)
            
            # Activate Sonic 
            if "sonic" in word.lower():
                speak("Yes?")
                
                # Stay Active until the user says "Stop Listening"
                while True : 
                    command = listen_for_command()
                    
                    if command is None :
                        continue
                                        
                    if "stop listening" in command.lower() :
                        speak("Going to Sleep")
                        break
                    
                    processCommand(command)
                                  
        except sr.UnknownValueError :
                    print("Could not understand the audio")
                    speak("Sorry, I didn't understand that!")
                      
        except sr.WaitTimeoutError :
                    print("You didn't say anything.")
                    speak("You didn't say anything")
                          
        except Exception as e:
                    print("Error:",type(e).__name__,e)