class abc:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def dtl(self):
        return f"{self.first}.{self.last}"

    @property
    def clgEmail(self):
        if self.first == None or self.last == None:
            return "Please Enter the Correct College Email"
        return f"{self.first}.{self.last}@qsc.com"

    @clgEmail.setter
    def clgEmail(self, str):
        lst = str.split("@")[0]
        self.first = lst.split(".")[0]
        self.last = lst.split(".")[1]

    @clgEmail.deleter
    def clgEmail(self):
       self.first = None
       self.last = None

a = abc("shan", "ali")

print(a.clgEmail)
a.first = "pk"

print(a.clgEmail)

print("Setters")
a.clgEmail = "new.shanali@clg.com"
print(a.clgEmail)
print(a.first)
print(a.last)

del a.clgEmail

print(a.clgEmail)

import inspect
print(inspect.getmembers(a))