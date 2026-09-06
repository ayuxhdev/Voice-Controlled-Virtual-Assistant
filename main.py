from dotenv import load_dotenv
import voice
import speech_recognition as sr
import commands
import ai

load_dotenv()
        
if __name__ == "__main__" :
    
    voice.speak("Initializing Sonic...... ")
    
    while True:
        
        r = sr.Recognizer()
        
        # Listen for the wake word "Sonic"
        # Obtain audio from the microphone
        
        print("Recognizing....")

        try: 
            with sr.Microphone() as source :
                
                print("Listening for the wake word......!")
                
                r.adjust_for_ambient_noise(
                    source,
                    duration=1
                    )
                
                audio = r.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=15
                    )
                
            word = r.recognize_google(audio)
            
            print("Recognized",word)
            
            # Activate Sonic 
            if "sonic" in word.lower():
                voice.speak("Yes Sir !")
                
                # Stay Active until the user says "Stop Listening"
                while True : 
                    command = voice.listen_for_command(r)
                    
                    if command is None :
                        continue
                                        
                    if "stop listening" in command.lower() :
                        ai.clear_conversation()
                        voice.speak("Going to Sleep")
                        break
                    
                    commands.processCommand(command)
                                  
        except sr.UnknownValueError :
                    print("Could not understand the audio")
                    voice.speak("Sorry, I didn't understand that!")
                      
        except sr.WaitTimeoutError :
                    print("You didn't say anything.")
                    voice.speak("You didn't say anything")
                          
        except Exception as e :
                    print("Error:",type(e).__name__,e)