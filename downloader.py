from pytube import Playlist, YouTube
from exceptions import InvalidLink


def download_from_youtube(link: str):
    try:
        if "playlist" in link:
            playlist = Playlist(link)
            for video in playlist.videos:
                video.streams.filter(file_extension='mp4').first().download(output_path="videos/")
        elif "watch" in link:
            video = YouTube(link)
            video.streams.filter(file_extension='mp4').first().download(output_path="videos/")
    except KeyError:
        raise InvalidLink
    else:
        raise InvalidLink
