from moviepy.editor import AudioFileClip
from os import listdir, path, remove, mkdir


def mp4_to_mp3():
    path_to_project = path.abspath("converter.py")[:-13]
    mkdir(path="spotify_tracks")
    
    for video in listdir("videos"):
        
        mp3_path = f'{path_to_project}/spotify_tracks/{video[:-1]}3'
        mp4_path = f'{path_to_project}/videos/{video}'
        
        mp4_file = AudioFileClip(mp4_path)
        mp4_file.write_audiofile(mp3_path, logger=None)
        print(video + " was successfull converted to mp3.")
        mp4_file.close()
        remove(mp4_path)
