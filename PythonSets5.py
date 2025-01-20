myset = set()
mySet1 = set([4, 24, 45, 6])

print(myset)
print(mySet1)

myset.add(24)
myset.add(23)
myset.add(64)
myset.add(100)

myset.remove(23)

# s3 = myset.union({23, 64})
s3 = myset.intersection({23, 64, 200})

print(myset)
print(s3)