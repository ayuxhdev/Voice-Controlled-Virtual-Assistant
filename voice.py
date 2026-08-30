import speech_recognition as sr
import pyttsx3 
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()

def speak_old(text) :
    engine.say(text)
    engine.runAndWait()
    
def speak(text) :
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
    
def listen_for_command(r) :
    
    try :
        # Listen for word 
        with sr.Microphone() as source :
            
            print("Sonic Activated! Listening for the command....")
            
            r.adjust_for_ambient_noise(
                source,
                duration=1)
            
            audio = r.listen(
                source,
                timeout = 10,
                phrase_time_limit = 15)
                            
                            
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
                                
    except Exception as e :
                print("Error:",type(e).__name__,e)
                return None