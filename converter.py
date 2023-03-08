from moviepy.editor import AudioFileClip
from os import listdir, path, remove


def mp4_to_mp3():
    main = path.abspath("converter.py")[:-13]
    for video in listdir("videos"):
        mp3_path = f'{main}/spotify_tracks/{video[:-1]}3'
        mp4_path = f'{main}/videos/{video}'
        mp4_file = AudioFileClip(mp4_path)
        mp4_file.write_audiofile(mp3_path)
        mp4_file.close()
        remove(mp4_path)
