from pytube import YouTube
from moviepy.editor import AudioFileClip
import tkinter as tk
from tkinter import filedialog
import os

def music_downloader(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        download_path = stream.download(output_path=save_path)
        mp3_path = download_path.replace(".mp4", ".mp3")
        audio = AudioFileClip(download_path)
        audio.write_audiofile(mp3_path)
        os.remove(download_path)  # remove the .mp4 file
        print("Music downloaded successfully!")
    
    except Exception as e:
        print("Error downloading video:", e)

def open_file_dialog():
    file_path = filedialog.askdirectory()
    return file_path


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    url = input("Enter the YouTube video URL: ")
    save_path = filedialog.askdirectory()
    print("Download started ...")

    music_downloader(url, save_path)