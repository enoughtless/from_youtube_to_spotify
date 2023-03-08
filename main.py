from downloader import download_from_youtube
from converter import mp4_to_mp3
from exceptions import InvalidLink

def main():
    link = input()
    
    try:
        download_from_youtube(link)  
    except InvalidLink:
        print("An error has occurred. Try again.")
        exit()
    
    mp4_to_mp3()
    print("Success.")
    

if __name__ == "__main__":
    main()
