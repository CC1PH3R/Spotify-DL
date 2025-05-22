import yt_dlp
import os

def download_audio(search_query: str, output_dir: str = "downloads"):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch1', # fetch only the first search result
        'quiet': False,
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"🔎 Searching for: {search_query}")
        ydl.download([search_query])