from gtts import gTTS
from pathlib import Path
from mutagen.mp3 import MP3
from rich.progress import track

def save_text_to_mp3(reddit_obj, video_length_max = 50):
    print("Yorumlar MP3 dosyasına çevriliyor")

    length = 0

    # Create a folder for the mp3 files.
    Path("assets/mp3").mkdir(parents=True, exist_ok=True)

    # video başlığı
    tts = gTTS(text=reddit_obj["thread_title"], lang="en", slow=False)
    tts.save(f"assets/mp3/title.mp3")
    length += MP3(f"assets/mp3/title.mp3").info.length

    #yorumlar
    for idx, comment in track(enumerate(reddit_obj["comments"]), "Saving..."):
        # ! Stop creating mp3 files if the length is greater than 50 seconds. This can be longer, but this is just a good starting point
        if length > video_length_max:
            break

        tts = gTTS(text=comment["comment_body"], lang="en", slow=False)

        tts.save(f"assets/mp3/{idx}.mp3")
        length += MP3(f"assets/mp3/{idx}.mp3").info.length

    print("Yorumlar Seslendirildi ve kaydedildi.")
    # ! Return the index so we know how many screenshots of comments we need to make.
    return length, idx
