from time import time

from pygame import mixer
from datetime import datetime

mixer.init()


def alarm(songName, userInput):
    mixer.music.load(songName)
    mixer.music.set_volume(1.0)
    mixer.music.play()

    while True:
        a = input()
        if a == userInput:
            mixer.music.stop()
            break


def currentTime(userInp):
    f = open("programmer.txt", "a")
    f.write(f"{userInp} {datetime.now()} \n")

currentWater = time()
currentEyes = time()
currentExercise = time()

water1 = 5
eyes1 = 22
exercise1 = 40

while True:

    if time() - currentWater > water1:

        print("Water Drinking Time... Press 's' to Stop the alarm")
        alarm('chupky.mp3', 's')
        currentWater = time()
        currentTime("Water Alarm Stops at :")


    elif time() - currentEyes > eyes1:

        print("Eyes Exercise Time... Press 's' to Stop the alarm")
        alarm('ranjish.mp3', 's')
        currentEyes = time()
        currentTime("Eyes Alarm Stops at :")

    elif time() - currentExercise > exercise1:

        print("Exercise Time... Press 's' to Stop the alarm")
        alarm('beInheha.mp3', 's')
        currentExercise = time()
        currentTime("Exercise Alarm Stops at :")

