from downloader import download_from_youtube
from converter import mp4_to_mp3
from exceptions import InvalidLink

def main():
    link = input()
    try:
        download_from_youtube(link)
        mp4_to_mp3()
    except InvalidLink:
        print("Invalid link")
    

if __name__ == "__main__":
    main()
