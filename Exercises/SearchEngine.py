listt = ["Shan is good with python", "Python is good than c", "python is python"]
inp = input("Search here\n")

for items in listt:
    items.split(" ")
    if inp == items:
        print(items)
