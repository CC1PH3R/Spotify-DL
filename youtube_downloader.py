import yt_dlp
import os

def download_audio(search_query: str, filename: str = None, output_dir: str = "downloads") -> str:
    os.makedirs(output_dir, exist_ok=True)

    base_name = filename if filename else '%(title)s'
    outtmpl = os.path.join(output_dir, base_name + '.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch1', # fetch only the first search result
        'quiet': False,
        'outtmpl': outtmpl,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
        ]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"🔎 Searching Youtube for: {search_query}")
        info = ydl.extract_info(search_query, download=True)
        downloaded_title = ydl.prepare_filename(info)
        mp3_path = os.path.splitext(downloaded_title)[0] + ".mp3"
        print(f"✅ Downloaded: {mp3_path}")
        return mp3_path