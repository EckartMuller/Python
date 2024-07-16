import pytube
class VideoIndir():
    def __init__(self):
        try:
            print("Video Downloader")
            url = str(input("Video Url: "))
            path = str(input("Video Path: "))
            resolution = str(input("Video Resolution: (High, Low): "))
            if (resolution == "High"):
                pytube.YouTube(url).streams.get_highest_resolution().download(path)
            elif (resolution == "Low"):
                pytube.YouTube(url).streams.get_lowest_resolution().download(path)
            else:
                print("Error")
        except:
            print("Error")


class SesIndir():
    def __init__(self):
        print("Audio Downloader")
        try:
            url = str(input("Audio Link: "))
            path = str(input("Audio  Path: "))
            pytube.YouTube(url).streams.get_audio_only().download(path)
        except:
            print("Error")
