from spotify_api import search_track
from youtube_downloader import download_audio
from tagger import embed_metadata
from fetch_and_download import safe_filename
import os

def download_song(query: str) -> str:
    metadata = search_track(query)
    title = metadata['title']
    artists = metadata['artists']
    album = metadata['album']
    cover_url = metadata['cover_url']

    search_query = f"{artists[0]} - {title}"
    safe_name = safe_filename(search_query)

    os.makedirs('downloads', exist_ok=True)
    downloaded_file = download_audio(search_query, safe_name)

    embed_metadata(
        file_path=downloaded_file,
        title=title,
        artists=artists,
        album=album,
        cover_url=cover_url
    )

    return downloaded_file