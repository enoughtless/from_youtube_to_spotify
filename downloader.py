from pytube import Playlist, YouTube
from exceptions import InvalidLink


def download_from_youtube(link: str):
    try:
        
        if "playlist" in link:
            some_playlist = Playlist(link)
            
            for video in some_playlist.videos:
                video.streams.filter(file_extension='mp4').first().download(output_path="videos/")
                print(video.title + " was successfull downloaded.")
        
        elif "watch" in link:
            video = YouTube(link)
            video.streams.filter(file_extension='mp4').first().download(output_path="videos/")
            print(video.title + " was successfull downloaded.")
            
    except Exception as e:
        print(e.__class__.__name__)
        raise InvalidLink
