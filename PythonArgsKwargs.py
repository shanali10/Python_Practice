def argsKwargs(normal, *args, **kwargs):
    print("Hello Arguments")
    for items in args:
        print(items)
    print(normal)
    print("\nNormal List\n")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

list = ["Shan", "Coder", "Ahmad", "Rider", "Arslan", "Shayar", "Parizaad", "Actor"]
normal = "I am Normal Function bro"
kw  = {"Shan": "Coder", "Ahmad": "Rider", "Arslan": "Shayar", "Parizaad": "Actor"}
argsKwargs(normal, *list, **kw)