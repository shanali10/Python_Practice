with open("shan2.txt") as f:
    a = f.readlines()
    print(a)

# file can be read or write multiple times in Python if we open file multiple times

f = open("shan2.txt")
a = f.readline()
print(a)

