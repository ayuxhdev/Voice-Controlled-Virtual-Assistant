import os

os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")

import webbrowser
from urllib.parse import quote
import yt_dlp
import vlc
import threading
import time

current_player = None

def search_web(query) :
    search_query = quote(query)
    url = f"https://www.google.com/search?q={search_query}"
    
    webbrowser.open(url)

def get_yt_result(song) :
    ydl_opts = {
        "quiet" : True,
        "extract_flat" : True        
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl :
        results = ydl.extract_info(
            f"ytsearch1:{song}",
            download = False
        )
        
    if results and results.get("entries") :
        return results["entries"][0]["url"]
    
    return None

def get_yt_audio(song) :
    
    download_dir = "music_cache"
    
    os.makedirs(download_dir,exist_ok=True)
    
    ydl_opts = {
        "quiet" : True,
        "format" : "bestaudio/best",
        "outtmpl" : f"{download_dir}/%(title)s[%(id)s].%(ext)s",
        "noplaylist" : True 
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl :
        results = ydl.extract_info(
            f"ytsearch1:{song}",
            download = False
        )
        
        if results and results.get("entries") :
            video = results["entries"][0]
            
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
            
            ydl.download([video_url])
            
            for filename in os.listdir(download_dir) :
                if video['id'] in filename :
                    return os.path.join(download_dir,filename)
                        
    return None

def play_audio(file_path) :
    global current_player
   
    file_path = os.path.abspath(file_path)
    
    current_player = vlc.MediaPlayer(file_path)
    
    player = current_player
    
    def cleanup() :
        time.sleep(0.5)
        
        player.release()
        
        if os.path.exists(file_path) :
            os.remove(file_path)
                    
        global current_player
                
        current_player = None
    
    def on_finish(event) :
        threading.Thread(
            target = cleanup,
            daemon = True
        ).start()
        
    event_manager = current_player.event_manager()
    event_manager.event_attach(
        vlc.EventType.MediaPlayerEndReached,
        on_finish
    )
        
    current_player.play()