import random
from win32com.client import Dispatch
def speak(str):
    sp = Dispatch("SAPI.SpVoice")
    sp.Speak(str)

print("\t --- Guss the Number Game ---\n")
print("You both have 10 Attempts Only\n")

speak("Player 1 Plays")
print("Player 1 Plays:")
a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))

ran = random.randint(a, b)

i = 1
j = 1
while i<=10:

    print(f"Guess the Number now between {a} and {b}\n")
    guess = int(input("Player 1: "))

    if guess > ran:
        print("Your Number is too large!")
        print(f"Attempts : {i}")
    elif guess < ran:
        print("Your number is too small!")
        print(f"Attempts : {i}")
    elif guess == ran:
        print(f"You got it in just {i} attempts")
        break

    i = i+1

    if i>10:
        print("\nYou did'nt Guess it!")

speak("Player 2 Plays")
print("\nPlayer 2 Plays:")
a1 = int(input("Enter the value of a\n"))
b1 = int(input("Enter the value of b\n"))
ran1 = random.randint(a, b)


while j <= 10:

    print(f"Guess the Number now between {a1} and {b1}\n")
    guess = int(input("Player 2: "))

    if guess > ran1:
        print("Your Number is too large!")
        print(f"Attempts : {j}")
    elif guess < ran1:
        print("Your number is too small!")
        print(f"Attempts : {j}")
    elif guess == ran1:
        print(f"You got it in just {j} attempts")
        break

    j = j + 1

    if j > 10:
        print("\nYou did'nt Guess it!")


print(f"\nPlayer 1 attempts = {i}\nPlayer 2 attempts = {j}")
if i > j:
    str = "Player 2 win"
    print(str)
    speak(str)
elif i < j:
    str = "Player 1 win"
    print(str)
    speak(str)

else:
    str = "Game tie"
    print(str)
    speak(str)