# def add(a,b):
#     return a+b

# add = lambda a,b: a+b

# print(add(34, 16))

def sortFunc(n):
    return n[1]

n = [[2, 65], [25, 22], [7, 55]]

n.sort(key=sortFunc)

print(n)