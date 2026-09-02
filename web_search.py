import webbrowser
from urllib.parse import quote

def search_web(query) :
    search_query = quote(query)
    url = f"https://www.google.com/search?q={search_query}"
    
    webbrowser.open(url)