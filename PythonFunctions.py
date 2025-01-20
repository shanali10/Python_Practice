def func1():
    print("Hellow Shan ALi Mughal")


func1()

def func2(a, b, c, d):
    result = (a*b+c)/d
    return result

print(func2(10, 20, 30, 5))

def func3():
    """ This is DocString of func3 in Python
    to know about the function code whenever we want to know"""


print(func3.__doc__)
print(func3.__sizeof__().__doc__)
