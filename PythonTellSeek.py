f = open("shan2.txt")
print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(15)
print(f.readline())
# print(f.tell())
f.seek(0)
print(f.readline())


f.close()