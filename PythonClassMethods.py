class Phone:
    calls = "Common"
    def __init__(self, name, camera, memory, ram):
        self.name = name
        self.camera = camera
        self.memory = memory
        self.ram = ram

    def attributes(self):
        return f"{self.name} has {self.camera} Camera, {self.memory} Memory and {self.ram} RAM"
    @classmethod
    def changeCalls(cls, newCalls):
        cls.calls = newCalls

    @classmethod
    def fromSlash(cls, string):
        return cls(*string.split("/"))

    @staticmethod
    def smartPhone():
        print('Smart Phones makes our life easier')

# samsung = Phone()
# iPhone = Phone()

# samsung.name = "Samsung"
# samsung.camera = "108 mp"
# samsung.memory = "256 GB"
# samsung.ram = "8 GB"
# samsung.calls

# iPhone.name = "iPhone"
# iPhone.camera = "12 mp"
# iPhone.memory = "1 TB"
# iPhone.ram = "8 GB"
# iPhone.calls

# print("Samsung List: ", samsung.__dict__)
# print("iPhone List: ", iPhone.__dict__)
#
# print(samsung.attributes())
# print(iPhone.attributes())


# USING CONSTRUCTOR

samsung = Phone("Samsung", "108MP", "256GB", "8GB")
iPhone = Phone("iPhone", "12MP", "1TB", "8GB")
#Class Methods as constructor Alternative
vivo = Phone.fromSlash("Vivo/32MP/64GB/4GB")

# print(samsung.attributes())
# print(iPhone.attributes())
print(vivo.attributes())
vivo.smartPhone()
# Phone.calls = "Not Common"

samsung.changeCalls("Samsung Calls")

# print(samsung.calls)
# print(Phone.calls)
# print(Phone.calls)