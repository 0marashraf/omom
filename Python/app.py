import pytube
print("Download video from web ")
url=input("Enter video URL :  ")
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')