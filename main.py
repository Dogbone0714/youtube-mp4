from pytube import YouTube
url = input("Enter the URL : ")
yt = YouTube(url)
video = yt.streams.first()
video.download()
print("Download Complete !")