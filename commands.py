import speech_recognition as sr
import webbrowser
import musicLibrary
import difflib
import os
import voice
import requests
import ai

newsapi_key = os.getenv("NEWS_API_KEY")

def processCommand(c) :
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
        voice.speak("Opening google")
        
    elif "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")
        voice.speak("Opening youtube")
        
    elif "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
        voice.speak("Opening instagram")
        
    elif "open facebook" in c.lower() :
        webbrowser.open("https://facebook.com")
        voice.speak("Opening facebook")
        
    elif "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")
        voice.speak("Opening linkedin")
        
    elif "play" in c.lower() :
        command = c.lower().replace("play", "").strip()
        matches = difflib.get_close_matches(
            command,
            musicLibrary.music.keys(),
            n=1,
            cutoff=0.5
            )
        
        if matches :
            song = matches[0]
            link = musicLibrary.music[song]
            webbrowser.open(link)
            voice.speak(f"Playing {song}")
            
        else :
            voice.speak("Please say the name of the song after 'play'.")
            
    elif "news" in c.lower() :
        try :
            voice.speak("Fetching the latest news for you.")
            print("Making request to NewsAPI...")
            
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}")

            if r.status_code == 200 :
                
                data = r.json()
                print("Response received from NewsAPI.")

                articles = data.get("articles", [])
                print(f"Found {len(articles)} articles.")

                if articles :
                    for i, article in enumerate(articles[:5]):
                        print(f"News {i+1}: {article['title']}")
                        voice.speak(article["title"])
                        
                else :
                    print("No articles found in the response.")
                    voice.speak("Sorry, I couldn't find any news.")
                    
            else :
                print(f"NewsAPI returned status code {r.status_code}")
                voice.speak("Unable to fetch news at the moment.")

        except Exception as e :
            print("Exception occurred while fetching news:", e)
            voice.speak("Something went wrong while fetching the news.")
                
    else :
        # Let Gemini handle the request 
        output = ai.aiProcess(c)
        voice.speak(output)