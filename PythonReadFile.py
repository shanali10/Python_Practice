f = open("shan.txt", "r")
# fileContent = f.read()
# print(fileContent)

# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readlines())

# print(f.readline(5))
# print(f.readline(10))

for line in f:
    print(line, end="")
