import random

randomNum = random.randint(1, 100)

print("Guess The Number \n You Have 10 Attempts \n")

i = 0

while (i<=10):
    i = i+1

    print("Enter Your Number")
    uNum = int(input())

    if uNum > randomNum:
        print("Your Number is Large!")

    elif uNum < randomNum:
        print("Your Number is Small!")
    else:
        print("You got it! in just ", i, "Attempts - WOW")
        break

    if i==10:
        print("Game Over!  Your Attempts are", i, " - YOU FAILED")
        break

