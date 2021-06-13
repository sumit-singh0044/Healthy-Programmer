from pygame import mixer
from datetime import datetime
from time import time

def eyeloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        S= input('Enter STOP to pause the music:\t')
        if S == 'STOP':
            mixer.music.stop()
            lognow("Eye realxed at: ")
            print("\nYou have done your eye exercise:\n")
            break

def waterloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        S= input('Enter STOP to pause the music:\t')
        if S == 'STOP':
            mixer.music.stop()
            lognow("Water drank at: ")
            print("\nYou have drink your water\n")
            break

def physicalloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        S= input('Enter STOP to pause the music:\t')
        if S == 'STOP':
            mixer.music.stop()
            lognow("Exercise done at: ")
            print("\nYou have your exercise\n")
            break

def lognow(data):
    with open("mylog.txt","a") as fk:
        fk.write(f"{data} {datetime.now()} \n")


if __name__ == '__main__':
    inti_eye= time()
    inti_water= time()
    inti_exercise= time()
    eye=30*60
    water=40*60
    exercise=45*60
    while True:
        if time()-inti_eye > eye:
            eyeloop('eye.mp3')
            inti_eye=time()
        if time()-inti_water > water:
            waterloop('water.mp3')
            inti_water=time()
        if time()-inti_exercise > exercise:
            physicalloop('physical.mp3')
            inti_exercise=time()