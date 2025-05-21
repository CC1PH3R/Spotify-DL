from dotenv import load_dotenv
load_dotenv()

import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Load cred from env
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Please set the SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.")

# Auth
auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = Spotify(auth_manager=auth_manager)

def fetech_track_info(spotify_url: str) -> dict:
    """ Given a Spotify URL, return key metatdata. """
    track = sp.track(spotify_url)
    return {
        'title': track['name'],
        'artists': [artist['name'] for artist in track['artists']],
        'album': track['album']['name'],
        'cover': track['album']['images'][0]['url']
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python spotify_api.py <spotify_url>")
        sys.exit(1)

    url = sys.argv[1]
    info = fetech_track_info(url)
    print(f"Title: {info['title']}")
    print(f"Artists: {', '.join(info['artists'])}")
    print(f"Album: {info['album']}")
    print(f"Cover: {info['cover']}")


