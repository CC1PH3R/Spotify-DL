from spotify_api import search_track
from youtube_downloader import download_audio
from tagger import embed_metadata
import sys
import os
import re

def safe_filename(name: str) -> str:
    """
    Sanitize the filename by replacing invalid characters.
    """
    # Replace invalid characters with underscores
    return re.sub(r'[\\/*?:"<>|]', "_", name)

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python fetch_and_download.py '<song name>'")
        sys.exit(1)

    query = sys.argv[1]

    # Get metadata from Spotify
    metadata = search_track(query)
    title = metadata["title"]
    artists = metadata["artists"]
    album = metadata["album"]
    cover_url = metadata["cover_url"]

    print(f"🎵 Track: {title}")
    print(f"🎤 Artist: {artists[0]}")
    print(f"💿 Album: {album}")

    # Create search query and safe filename
    search_query = f"{artists[0]} - {title}"
    safe_name = safe_filename(f"{artists[0]} - {title}")

    # Create download directory if it doesn't exist
    os.makedirs("downloads", exist_ok=True)

    # Download the audio from YouTube
    print(f"🔍 Downloading: {search_query}")
    try:
        downloaded_file = download_audio(search_query, safe_name)
        print(f"✅ Downloaded: {downloaded_file}")
        
        # Embed metadata
        embed_metadata(
            file_path=downloaded_file,
            title=title,
            artists=artists,
            album=album,
            cover_url=cover_url
        )
        print(f"✅ Metadata embedded successfully.")
        
    except Exception as e:
        print(f"❌ Error during download: {e}")
        sys.exit(1)