#import the package

from pytube import YouTube

#enter URL

url='https://www.youtube.com/watch?v=tQFs8q89eXE'

myvideo=YouTube(url)

#print title of the video

print(myvideo.title)

#return thumbnail link

print(myvideo.thumbnail_url)

#set highest resolution

myvideo=myvideo.streams.get_highest_resolution()

#download 

myvideo.download()
