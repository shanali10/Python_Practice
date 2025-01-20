count = ["34", "03", "88"]

# normal way

# for i in range(len(count)):
#     count[i] = int(count[i])
#
# count[1] = count[1] + 7
#
# print(count)

# ..... Map .....

count = list(map(int, count))
count[1] = count[1] + 7
print(count)

def sq(r):
    return r*r

l2 = [3, 4, 2, 10]
l2 = list(map(sq, l2))
print("squre")
print(l2)

l3 = [4,9,2,1,5]
l3 = list(map(lambda x:x*x, l3))
print(f"Lambda\n {l3}")


print("Using Multi Functions in map")

def sqr (a):
    return a*a

def cube (b):
    return b*b*b

funcList = [sqr, cube]

for i in range(10):
    tog = list(map(lambda x:x(i), funcList))
    print(tog)


    # .......... Filter .....

print("Now Using Filter")

l4 = [4, 5, 100, 10, 3, 2,  9, 20]

def grt9(num):
    return num>5
list4 = list(filter(grt9, l4))

print(list4)


#........... Reduce ...........

from functools import reduce
print("\nNow Using Reduce")

l5 = [10, 4, 5, 8, 3]
list5 = reduce(lambda x,y: x+y, l5)

print(list5)
