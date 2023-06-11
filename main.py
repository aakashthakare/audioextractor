import os.path
import moviepy.editor as mp
import time

from pathlib import Path

if __name__ == '__main__':
    print("Extracting MP3 from the MP4 Video.")

    video = mp.VideoFileClip(r"video/loren-ipsum.mp4")

    if not os.path.exists("output"):
        os.mkdir("output")

    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = Path(video.filename).stem
    video.audio.write_audiofile(rf"output/audio_extract_{filename}_{timestamp}.mp3")

    print(f"Extracted audio file is created under output directory.")
