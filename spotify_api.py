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


def search_track (query: str) -> dict:
    """ Search for a track on Spotify and return its metadata. """
    results = sp.search(q=query, type='track', limit=1)

    if not results['tracks']['items']:
        raise Exception(f"No results found for your '{query}'")
    
    track = results['tracks']['items'][0]

    # Get the best quality album cover
    cover_url = None
    if track['album']['images']:
        cover_url = track['album']['images'][0]['url']

    return {
        'title': track['name'],
        'artists': [artist['name'] for artist in track['artists']],
        'album': track['album']['name'],
        'cover_url': cover_url
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python spotify_api.py <song name>")
        sys.exit(1)

    query = sys.argv[1]
    info = search_track(query)
    print(f"Title: {info['title']}")
    print(f"Artists: {', '.join(info['artists'])}")
    print(f"Album: {info['album']}")
    print(f"Cover: {info['cover_url']}")