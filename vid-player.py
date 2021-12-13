#!/usr/bin/env python3

# Title: Vid Player
# Description: Having a list of fav songs, add them to a file or supply it as arg with -f and let this play all of them for you.
# Author: Kelvin <email@gmail.com>
# Date: 2021-12-07
# Version: 1.0.0

# Imports
import os
import sys
from shutil import which
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--single', help='Provide a single video file with full path. ( Optional )')
parser.add_argument('-f', '--file', help='Provide a Filename with your videos path. ( Optional )')

args = parser.parse_args()
video = args.single
vf = args.file

def python_chk():
    if sys.version_info < (3, 5):
        sys.stderr.write("Your need a higher python version to use the script")
        sys.exit(1)

def program_chk():
    """Ensures that mpv is installed before doing anything else. Also asks if you want to install"""
    program = ['mpv']
    for i in program:
        installed = which(i)
        if installed == None:
            print(f"Install {i} to use this script!")
            # x = input("Do you want to install now?[y,n]: ")
            # if x == 'y':
            #     os.system(f"sudo apt install {i}")
            # else:
            #     pass
            sys.exit(1)
        else:
            pass

def user_file(vf):
    video_file(file_name = vf)

def video_file(file_name = 'files.txt'):
    """This gets the video file names in a file.txt and return an array of them"""
    with open(file_name, 'r') as videos:
        video = []
        for v in videos.readlines():
            video.append(v.strip())
    return video
                
def player(video, isList = True):
    """This is where the program mpv is used to play each video individually"""
    if isList:
        for i in video:
            os.system('mpv ' + i + ' 1>/dev/null')
    else:
        os.system('mpv ' + video + ' 1>/dev/null')
        pass

def main():
    python_chk()
    program_chk()
    
    if args.single:
        player(video, isList = False)
    elif args.file:
        user_file(vf)
    else:
        player(video_file())

if __name__ == '__main__':
    main()