from pytube import YouTube
from moviepy.editor import AudioFileClip
import tkinter as tk
from tkinter import filedialog
import os

def music_downloader(url, save_path):
    """Downloads audio from a YouTube video and saves it in MP3 format."""

    try:
        # Get YouTube video details
        yt = YouTube(url)

        # Get only the audio
        stream = yt.streams.get_audio_only()

        # Download the audio
        download_path = stream.download(output_path=save_path)

        # Converting the original .mp4 into .mp3
        mp3_path = download_path.replace(".mp4", ".mp3")
        audio = AudioFileClip(download_path)
        audio.write_audiofile(mp3_path)
        os.remove(download_path)  # remove the .mp4 file
        print("Music downloaded successfully!")
    
    except Exception as e:
        # Handle any errors that may occur during the process
        print(f"Error downloading video: {e}")

def open_file_dialog():
    """Opens a file dialog to select a directory."""
    file_path = filedialog.askdirectory()
    return file_path


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # Get YouTube video URL from user input
    url = input("Enter the YouTube video URL: ")

    # Choose the directory to save the downloaded audio
    save_path = filedialog.askdirectory()

    print("Download started ...")

    # Call the music_downloader function with the provided URL and save path
    music_downloader(url, save_path)