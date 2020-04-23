import pytube
import sys
import os
import subprocess
print("-YouTube Downloader-")
print("This is very very fast! and no ads!")
print("-Made by pdg916-")
print("정말 빠릅니다. 광고도 없어요. 많이 이용해주세요.ㅎ")
print("")
while True:
    print("1: mp3")
    print("2: mp4")
    print("3: End")
    sel=input(":")
    print("")
    if sel=="1":
        print("Enter the YouTube URL.")
        data=input(":")
        print("")
        yt=pytube.YouTube(data)
        vid=yt.streams.filter(type="audio")
        for i in range(len(vid)):
            print(i,'. ',vid[i])
        print("Please select the sound quality to download. [Enter number]")
        vnum=int(input(":"))
        print("")
        print("Please enter a storage location. Example) C:\유튜브저장소")
        pa=input(":")
        parent=pa
        vid[vnum].download(parent)
        print("Saved successfully.")
        continue
    elif sel=="2":
        print("Enter the YouTube URL.")
        data1= input(":")
        print("")
        yt1 = pytube.YouTube(data1)
        vid1 = yt1.streams.filter(type="video")
        for i in range(len(vid1)):
            print(i, '. ', vid1[i])
        print("Please select a quality to download. [Enter number]")
        vnum1 = int(input(":"))
        print("")
        print("Please enter a storage location. Example) C:\유튜브저장소")
        pa1 = input(":")
        parent1 = pa1
        vid1[vnum1].download(parent1)
        print("Saved successfully.")
        continue
    elif sel=="3":
        break
    else:
        print("Enter 1[mp3] or 2[mp4] or 3[end].")
        continue