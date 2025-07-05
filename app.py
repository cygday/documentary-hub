
import os
import requests

from flask import Flask, render_template

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
    "part": "snippet",
    "q": query,
    "type": "video",
    "maxResults": 5,
    "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    video_ids = [item["id"]["videoId"] for item in data.get("items", [])]
    return video_ids

@app.route('/')
def index():
    videos = search_youtube("documentary")
    return render_template("index.html", videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
