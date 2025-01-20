def func2(func1):
    def ex():
        print("Running ex")
        func1()
        print("Now Running Function")
    return ex()

@func2
def funcInFunc():
    print("Hello Decorator Function")

