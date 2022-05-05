import pafy

print("Video token: ", end="")
token = input()
video = pafy.new(token)
preview = video.getbestthumb()
author = video.author
title = video.title
duration = video.duration
best = video.getbestaudio()
audio = best.url
print("Preview link: " + preview)
print("Channel name: " + author)
print("Video name: " + title)
print("Duration: " + duration)
print("Audio link: " + audio)
