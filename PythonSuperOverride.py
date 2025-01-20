class Y:
    a = 55
    def __init__(self):
        self.me = "I am Shan in class Y"
        self.you = 34
        self.new = "New Variable in class Y"

class Z(Y):
    a = 59

    def __init__(self):

        # super().__init__()
        self.me = "I am Shan in class Z"
        self.you = 34
        self.zz = 100
        super().__init__()


a = Y()
b = Z()

print(a.a, a.you, a.me)
print(b.a, b.me, b.you, b.zz, b.new)
