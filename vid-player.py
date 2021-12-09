#!/usr/bin/env python3

# Title: Vid Player
# Description: Having a list of fav songs, add them to a file and let this play all of them for you.
# Author: Kelvin <email@gmail.com>
# Date: 2021-12-07
# Version: 1.0.0

# Imports
import os
import sys
from shutil import which

def program_chk():
    """Ensures that mpv is installed before doing anything else. Also asks if you want to install"""
    program = ['mpv']
    for i in program:
        installed = which(i)
        if installed == None:
            print(f"Install {i} to use this script!")
            x = input("Do you want to install now?[y,n]: ")
            if x == 'y':
                os.system(f"sudo apt install {i}")
            else:
                pass
            sys.exit()
        else:
            pass

def video_file():
    """This gets the video file names in a file.txt and return an array of them"""
    with open('files.txt', 'r') as videos:
        video = []
        for v in videos.readlines():
            video.append(v.strip())
    return video
                
def player(video):
    """This is where the program mpv is used to play each video individually"""
    for i in video:
        os.system('mpv ' + i + ' 1>/dev/null')

def main():
    program_chk()
    player(video_file())

if __name__ == '__main__':
    main()