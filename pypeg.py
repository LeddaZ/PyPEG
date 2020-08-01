# PyPEG
# Python script to transcode videos with ffmpeg

# Import required modules
import os
import platform
import time

# Set correct slash because Windows has to be
# different obv :/
if platform.system() == "Windows":
    s="\\"
elif platform.system() == "Darwin":
    s="/"
elif platform.system() == "Linux":
    s="/"

# Function that runs "cls" to clear console on Windows,
# "clear" on macOS/Linux
def clean():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin":
        os.system('clear')
    elif platform.system() == "Linux":
        os.system('clear')

# Main menu
def menu():
    clean()
    print("###################")
    print("###### PyPEG ######")
    print("###################")
    print()
    print("A simple Python ffmpeg script by LeddaZ")
    print()
    print("What do you want to do?")
    print()
    print("(C)onvert a video")
    print("(P)lay a video with ffplay")
    print("Get (i)nfo for a video file")
    print("(Q)uit and go play outside")
    print()
    print("Your option:")
    # Read user input, go back to main menu
    # on invalid option
    opt = input()
    if opt.lower() == "c":
        convert()
    elif opt.lower() == "p":
        play()
    elif opt.lower() == "i":
        info()
    elif opt.lower() == "q":
        bye()
    else:
        clean()
        menu()

# Convert a video
def convert():

    # Yes or no
    def yesno():
        print("Is everything correct? (y/n)")
        ans=input()
        if ans.lower() == "y":
            ff()
        elif ans.lower() == "n":
            convert()
        else:
            print("Invalid option.")
            yesno()

    # ffmpeg command
    def ff():
        cmdline="ffmpeg -hide_banner -i " + srcpath + " -c:v libx264 -preset slow -crf 22 -c:a copy " + outpath + s + outname + "." + outext
        os.system(cmdline)

    clean()
    print("###################")
    print("# Convert a video #")
    print("###################")
    print()
    print("Source file path:")
    srcpath=input()
    print()
    print("Output file name:")
    outname=input()
    print()
    print("Output file format:")
    outext=input()
    print()
    print("Output file path:")
    outpath=input()
    print()
    yesno()
    clean()
    print("Done! Returning to main menu in 5 seconds...")
    time.sleep(5)
    menu()

# Play a video
def play():

    # ffplay command
    def ffp():
        cmdline="ffplay -hide_banner " + srcpath
        os.system(cmdline)

    clean()
    print("################")
    print("# Play a video #")
    print("################")
    print()
    print("Source file path:")
    srcpath=input()
    ffp()
    clean()
    print("Done! Returning to main menu in 5 seconds...")
    time.sleep(5)
    menu()

# Get info with ffprobe
def info():

    # ffprobe command
    def probe():
        cmdline="ffprobe -hide_banner " + srcpath
        os.system(cmdline)

    clean()
    print("##################")
    print("# Get video info #")
    print("##################")
    print()
    print("Source file path:")
    srcpath=input()
    clean()
    probe()
    print()
    print("Press any key to return to main menu...")
    input()
    menu()

# Change da world
# my final message
# Good b ye.
def bye():
    clean()
    print("Goodbye!")
    time.sleep(1)
    quit()

# Print main menu
menu()