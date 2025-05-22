from spotify_api import fetech_track_info
from youtube_downloader import download_audio
import sys

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python fetch_and_download.py <spotify_track_url>")
        sys.exit(1)

    spotify_url = sys.argv[1]
    metadata = fetech_track_info(spotify_url)

    title = metadata["title"]
    artists = metadata["artists"]
    search_query = f"{artists[0]} - {title}"

    print(f"🎵 Track: {title}")
    print(f"🎤 Artist: {artists[0]}")
    print(f"🔍 Searching YouTube for: {search_query}")

    download_audio(search_query)
    print("✅ Download complete.")
    print("🎵 Track: ", metadata["title"])
    print("🎤 Artist: ", metadata["artists"][0])