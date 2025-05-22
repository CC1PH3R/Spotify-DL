from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC
import requests

def embed_metadata(file_path, title, artists, album, cover_url):
    audio = MP3(file_path, ID3=ID3)

    try:
        audio.add_tags()
    except Exception:
        pass # tags already exist

    audio.tags["TIT2"] = TIT2(encoding=3, text=title)  # Title
    audio.tags["TPE1"] = TPE1(encoding=3, text=", ".join(artists))  # Artist
    audio.tags["TALB"] = TALB(encoding=3, text=album)  # Album

    # Download album art
    image_data = requests.get(cover_url).content

    audio.tags["APIC"] = APIC(
        encoding=3,  # 3 is for UTF-8
        mime="image/jpeg",  # Image MIME type
        type=3,  # 3 is for the cover image
        desc="Cover",
        data=image_data,
    )

    audio.save()
    print(f"✅ Metadata embedded into: {file_path}")
