class Phone:
    calls = "Common"
    def __init__(self, name, camera, memory, ram):
        self.name = name
        self.camera = camera
        self.memory = memory
        self.ram = ram

    def attributes(self):
        return f"{self.name} has {self.camera} Camera, {self.memory} Memory and {self.ram} RAM"

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

print(samsung.attributes())
print(iPhone.attributes())