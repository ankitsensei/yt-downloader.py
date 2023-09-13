from pytube import YouTube
link = input("Link: ")

choose = input('''
            1. Audio Only
            2. Video
            3. Cancel
               :''')
video = YouTube(link)

if choose == "1":
    video.streams.get_audio_only().download()
    print("Audio Downloaded")
elif choose == "2":
    video.streams.get_highest_resolution().download()
    print("Video Downloaded")
elif choose == "3":
    print("Cancelled")
else:
    print("Wrong Input!! Operation failed.")