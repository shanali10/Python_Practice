print("Shan's Health Management System\n")
print("Press 1 for Aryan\n Press 2 for Shan ALi\n Press 3 for Alyan\n")
name = int(input())


def getTime():
    import datetime
    return datetime.datetime.now()

# Aryan Files

def aryanFoodFileWrite():
    print("Now you can Update your Food data")
    aryanFoodData = input() + "\n"

    f = open("AryanFood.txt", "a")
    f.write(str([str(getTime())]) + ": " + aryanFoodData)

def aryanFoodFileRead():
    f = open("AryanFood.txt", "r")
    a = f.read()
    print(a)


def aryanDietFileWrite():
    print("Now you can Update your Diet data")
    aryanDietData = input() + "\n"
    f = open("AryanDiet.txt", "a")
    f.write(str([str(getTime())]) + ": " + aryanDietData)

def aryanDietFileRead():
    f = open("AryanDiet.txt", "r")
    a = f.read()
    print(a)



# Shan Files

def shanAliFoodFileWrite():
    print("Now you can Update your Food data")
    shanFoodData = input() + "\n"
    f = open("ShanAliFood.txt", "a")
    f.write(str([str(getTime())]) + ": " + shanFoodData)

def shanAliFoodFileRead():
    f = open("ShanAliFood.txt", "r")
    a = f.read()
    print(a)


def shanAliDietFileWrite():
    print("Now you can Update your Diet data")
    shanDietData = input() + "\n"
    f = open("ShanAliDiet.txt", "a")
    f.write(str([str(getTime())]) + ": " + shanDietData)

def shanAliDietFileRead():
    f = open("ShanAliDiet.txt", "r")
    a = f.read()
    print(a)


#     Alyan Files

def alyanFoodFileWrite():
    print("Now you can Update your Food data")
    alyanFoodData = input() + "\n"
    f = open("AlyanFood.txt", "a")
    f.write(str([str(getTime())]) + ": " + alyanFoodData)

def alyanFoodFileRead():
    f = open("AlyanFood.txt", "r")
    a = f.read()
    print(a)


def alyanDietFileWrite():
    print("Now you can Update your Diet data")
    alyanDietData = input() + "\n"
    f = open("AlyanDiet.txt", "a")
    f.write(str([str(getTime())]) + ": " + alyanDietData)

def alyanDietFileRead():
    f = open("AlyanDiet.txt", "r")
    a = f.read()
    print(a)




if name == 1:
    print("Do you want to add data About Food or Diet?")
    print("Press 1 for Food\nPress 2 for Diet")
    fileType1 = int(input())
    if fileType1 == 1:
        aryanFoodFileWrite()
        print(str([str(getTime())]),"- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile1 = int(input())

        if readFile1 == 1:
            aryanFoodFileRead()
        elif readFile1 == 0:
            exit()

    if fileType1 == 2:
        aryanDietFileWrite()
        print(str([str(getTime())]), "- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile1 = int(input())

        if readFile1 == 1:
            aryanDietFileRead()
        elif readFile1 == 0:
            exit()



elif name == 2:
    print("Do you want to add data About Food or Diet?")
    print("Press 1 for Food\nPress 2 for Diet")
    fileType2 = int(input())
    if fileType2 == 1:
        shanAliFoodFileWrite()
        print(str([str(getTime())]),"- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile2 = int(input())

        if readFile2 == 1:
            shanAliFoodFileRead()
        elif readFile2 == 0:
            exit()

    if fileType2 == 2:
        shanAliDietFileWrite()
        print(str([str(getTime())]), "- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile2 = int(input())

        if readFile2 == 1:
            shanAliDietFileRead()
        elif readFile2 == 0:
            exit()



elif name == 3:
    print("Do you want to add data About Food or Diet?")
    print("Press 1 for Food\nPress 2 for Diet")
    fileType3 = int(input())
    if fileType3 == 1:
        alyanFoodFileWrite()
        print(str([str(getTime())]),"- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile3 = int(input())

        if readFile3 == 1:
            alyanFoodFileRead()
        elif readFile3 == 0:
            exit()

    if fileType3 == 2:
        alyanDietFileWrite()
        print(str([str(getTime())]), "- You have Successfully Updated Your data")
        print("Do you want to read About Your Health?")
        print("Press 1 for Yes and 0 for No")
        readFile3 = int(input())

        if readFile3 == 1:
            alyanDietFileRead()
        elif readFile3 == 0:
            exit()

