from spotify_api import fetch_track_info
from youtube_downloader import download_audio
from tagger import embed_metadata
import sys
import glob
import os

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python fetch_and_download.py <spotify_track_url>")
        sys.exit(1)

    spotify_url = sys.argv[1]
    metadata = fetch_track_info(spotify_url)

    title = metadata["title"]
    artists = metadata["artists"]
    search_query = f"{artists[0]} - {title}"

    print(f"🎵 Track: {title}")
    print(f"🎤 Artist: {artists[0]}")
    print(f"🔍 Searching YouTube for: {search_query}")

    download_audio(search_query)
    print("✅ Download complete.")

# Find the most recent MP3 in downloads/
downloaded_files = sorted(glob.glob("downloads/*.mp3"), key=os.path.getmtime, reverse=True)

if downloaded_files:
    mp3_file = downloaded_files[0]
    print(f"📥 Found downloaded file: {mp3_file}")
    embed_metadata( 
        mp3_file,
        title=metadata["title"],
        artists=metadata["artists"],
        album=metadata["album"],
        cover_url=metadata["cover_url"]
    )
else:
    print("❌ No downloaded MP3 files found in downloads/")
    sys.exit(1)
print("✅ Metadata embedded successfully.") 