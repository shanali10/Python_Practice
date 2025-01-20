print("What computation do you want to do? ",
      "\n Addition \n Subtraction \n Multiplication \n Division")
computation = input()

if computation == "Addition" or computation == "addition":

    print("Enter 1st Number")
    ad1 = int(input())
    print("Enter 2nd Number")
    ad2 = int(input())

    if ad1==56 or ad1==9 and ad2==56 or ad2==9:
        print("77")
    else:
        print("Result =", ad1 + ad2)

elif computation == "Multiplication" or computation == "multiplication":

    print("Enter 1st Number")
    ml1 = int(input())
    print("Enter 2nd Number")
    ml2 = int(input())

    if ml1 == 45 or ml1 == 3 and ml2 == 45 or ml2 == 3:
        print("555")
    else:
        print("Result =", ml1 * ml2)


elif computation == "Division" or computation == "division":

    print("Enter 1st Number")
    dv1 = int(input())
    print("Enter 2nd Number")
    dv2 = int(input())

    if dv1 == 56 and dv2 == 6:
        print("4")
    else:
        print("Result =", dv1 / dv2)


elif computation == "Subtraction" or computation == "subtraction":

    print("Enter 1st Number")
    sub1 = int(input())
    print("Enter 2nd Number")
    sub2 = int(input())

    if sub1 == 80 and sub2 == 37:
        print("101")
    else:
        print("Result =", sub1 - sub2)

else:
    print("Please Choose Correct Computation")