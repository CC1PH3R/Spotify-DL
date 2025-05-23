import os
import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, APIC, ID3NoHeaderError

def embed_metadata(file_path: str, title: str, artists: list, album: str, cover_url: str):
    """
    Embed metadata into an MP3 file.
    """
    try:
        # Load the MP3 file
        audio = MP3(file_path)

        # add ID3 tags if they don't exist
        try:
            audio.add_tags()
        except Exception:
            pass # ID3 tags already exist

        # Set metadata
        audio.tags.add(TIT2(encoding=3, text=title))  # Title
        audio.tags.add(TALB(encoding=3, text=album))  # Album
        audio.tags.add(TPE1(encoding=3, text=artists))  # Artist

        # Download and embed cover art
        if cover_url:
            try:
                response = requests.get(cover_url, timeout=10)
                if response.status_code == 200:
                    audio.tags[APIC] = APIC(
                        encoding=3,
                        mime='image/jpeg',
                        type=3,  # Cover (front)
                        desc='Cover',
                        data=response.content
                    )
                    print("🖼️ Album cover embedded successfully.")
            except Exception as e:
                print(f"⚠️ Could not embed album cover: {e}")
        
        # Save the changes
        audio.save()
        print(f"✅ Metadata embedded for: {title}")
        
    except Exception as e:
        print(f"❌ Error embedding metadata: {e}")

if __name__ == "__main__":
    # Test the tagger function
    print("This is the tagger module. Import it to use embed_metadata function.")