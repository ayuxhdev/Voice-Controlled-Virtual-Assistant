import webbrowser
import os
import voice
import requests
import ai
import web_search

newsapi_key = os.getenv("NEWS_API_KEY")

def strip_keyword(c, keyword) :
    words = c.split()
    
    if keyword in words :
        words.remove(keyword)
        
    return " ".join(words)

def detect_intent(c):
    c = c.lower().strip()
    words = c.split()
    
    if "open" in words :
        target = c.replace("open","",1).strip()
        return "open", target
    
    elif "search" in words or "find" in words :
        
        if "search" in words :
            query = c.replace("search","",1).strip()
        
        else :
            query = c.replace("find","",1).strip()
            
        if query.startswith("for ") :
            query = query[4:].strip()
            
        return "search", query
    
    elif "play" in words :
        target = c.replace("play","",1).strip()
        return "play", target
    
    elif "news" in words :
        return "news", ""
    
    return "unknown", c

def processCommand(c) :
    
    c = c.lower().strip()
    intent, target = detect_intent(c)
    
    print("Intent:", intent)
    print("Target:", target)
    
    if intent == "open" :
        if "google" in target :
            webbrowser.open("https://google.com")
            voice.speak("Opening google")
            
        elif "youtube" in target :
            webbrowser.open("https://youtube.com")
            voice.speak("Opening youtube")
            
        elif "instagram" in target :
            webbrowser.open("https://instagram.com")
            voice.speak("Opening instagram")
            
        elif "facebook" in target :
            webbrowser.open("https://facebook.com")
            voice.speak("Opening facebook")
            
        elif "linkedin" in target :
            webbrowser.open("https://linkedin.com")
            voice.speak("Opening linkedin")
            
        elif target :
            web_search.search_web(target)
            voice.speak(f"Searching for {target}")
            
        else :
            voice.speak("What would you like me to open ?")
        
    elif intent == "play" :
        song = target
        
        if song :
            search_query = song.replace(" ", "+")
            youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
            
            webbrowser.open(youtube_url)
            voice.speak(f"Searching Youtube for {song}")
            
        else :
            voice.speak("Please say the name of the song after play")
            
    elif intent == "search" :
        if target :
            web_search.search_web(target)
            voice.speak(f"Searching for {target}")
        
        else :
            voice.speak("What do you like me to search for ?")
            
    elif intent == "news" :
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