import random


print("Snake - Water - Gun --- Full Game")
print("Computer has already choose one of the given options")
print("You people have 10 attempts to Play")

i = 9
player = 0
com = 0
tie = 0

while (i>=0):

    gameItems = ["snake", "water", "gun"]
    ran = random.choice(gameItems)
    print("Press s for Snake\n Press w for Water\n Press g for Gun\n")
    userChoice = str(input())

    if ran == "snake" and userChoice == 's':
        print(f"Game Tie!    Remaining = {i}")
        print(f"Your Points = {player}       Computer Points = {com}")
        tie = tie+1
        print()

    elif ran == "water" and userChoice == 'w':
        print(f"Game Tie!   Remaining = {i}")
        print(f"Your Points = {player}       Computer Points = {com}")
        tie = tie+1
        print()

    elif ran == "gun" and userChoice == "g":
        print(f"Game Tie!   Remaining = {i}")
        print(f"Your Points = {player}       Computer Points = {com}")
        tie = tie+1
        print()

    elif ran == "snake" and userChoice == 'w':
        print(f"Computer Won!    Remaining = {i}")
        com = com+1
        print(f"Your Points = {player}       Computer Points = {player}")
        print()

    elif ran == "snake" and userChoice == 'g':
        print(f"You Won!    Remaining = {i}")
        player = player+1
        print(f"Your Points = {player}       Computer Points = {com}")
        print()

    elif ran == "water" and userChoice == 's':
        print(f"You Won!    Remaining = {i}")
        player = player+1
        print(f"Your Points = {player}       Computer Points = {com}")
        print()

    elif ran == "water" and userChoice == 'g':
        print(f"Computer Won!   Remaining = {i}")
        com = com+1
        print(f"Your Points = {player}       Computer Points = {com}")
        print()

    elif ran == "gun" and userChoice == 's':
        print(f"Computer Won!   Remaining = {i}")
        com = com+1
        print(f"Your Points = {player}       Computer Points = {com}")
        print()

    elif ran == "gun" and userChoice == 'w':
        print(f"You Won!     Remaining = {i}")
        player = player+1
        print(f"Your Points = {player}       Computer Points = {com}")
        print()

    else:
        print("Please Input Valid Options")
        print()

    i = i-1

    if (i<0):
        if player>com:
            print(f"\nCongrats You Won the Series! ... Points = {player}")
            print(f"Computer loose the Series! ... Points = {com}")
            print(f"Total Game Tie for {tie} times")

        elif player<com:
            print(f"\nComputer Won the Series! ... Points = {com}")
            print(f"You loose the Series! ...  Points = {player}")
            print(f"Total Game Tie for {tie} times")

        else:
            print("\nGame draw")
            print(f"Computer Points = {com}")
            print(f"Your Points = {player}")
            print(f"Total Game Tie for {tie} times")
