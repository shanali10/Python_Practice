print("Press 1 for Triangular Star Pattern\n",
      "Press 2 for Reverse Triangular Star Pattern")
starPattern = int(input())

num = int(input("Enter any Number to print star Pattern\n"))

count = 0
count1 = 0

if starPattern == 1:

    for count in range(1, num + 1):
        for count1 in range(1, count+1):
            print("*", end="")
        print()

elif starPattern == 2:

    for count in range(num, 0, -1):
        for count1 in range(1, count+1):
            print("*", end="")
        print()


