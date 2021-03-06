from random import randrange

from yt_dlp import YoutubeDL

from pathlib import Path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip


def get_start_and_end_times(video_length, length_of_clip):

    random_time = randrange(180, int(length_of_clip) - int(video_length))
    return random_time, random_time + video_length


def download_background():
    """Downloads the background video from youtube.

    Shoutout to: bbswitzer (https://www.youtube.com/watch?v=n_Dv4JMiwK8)"""
    

    if not Path("assets/mp4/background.mp4").is_file():
        print(
            "Minecraft arkaplan videosu bulunamadı, bu indirme işlemi 1 kez yapılacaktır."
        )

        print("Arka plan videosu indiriliyor. çatlamayın, 1 kere yapılacak bir işlem")

        ydl_opts = {
            "outtmpl": "assets/mp4/background.mp4",
            "merge_output_format": "mp4",
            "quality": "1080"
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v=n_Dv4JMiwK8")

        print("Arka plan videosu başarıyla indirildi")


def chop_background_video(video_length):
    print("Video için arkaplan videosu kırpılıyor")
    background = VideoFileClip("assets/mp4/background.mp4")

    start_time, end_time = get_start_and_end_times(video_length, background.duration)
    ffmpeg_extract_subclip(
        "assets/mp4/background.mp4",
        start_time,
        end_time,
        targetname="assets/mp4/clip.mp4",
    )
    print("ArkaPlan için video kırpıldı")
