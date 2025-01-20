import time

def corontines():
    str = "This is Shan Ali Mughal and this is my laptop if you want to search here you can search " \
          "easily.. Good luck to all of you"
    time.sleep(3)


    while True:
        let = (yield)
        if let in str:
            print(f"{let} : Founded")
        else:
            print(f"{let} : not Found")


ins = corontines()
next(ins)
while True:
    print("What do you want to find?")
    f = input()
    ins.send(f)

    if f == "break":
        break