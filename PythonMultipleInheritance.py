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
    def nokia():
        print("Nokia is an example of Phone")



class SmartPhone():

    def __init__(self, name, camera, memory, ram, network):
        self.name = name
        self.camera = camera
        self.memory = memory
        self.ram = ram
        self.network = network
    def smartDetails(self):
        return f"{self.name} has {self.camera} Camera, {self.memory} Memory, {self.ram} RAM and {self.network} Available"


class meta(Phone, SmartPhone):
    def metaOwner(self):
        print("Facebook")

nokia = Phone("Nokia", "2000mAH", "50MB", "0.5MP")
qMobile = Phone("qMobile", "1200mAH", "8MB", "0.01MP")
#Class Methods as constructor Alternative
china = Phone.fromSlash("China/600mAH/1024KB/0.000005MP")

iPhone = SmartPhone("iPHone", "4200mAH", "1TB", "12MB", "5G")

# print(iPhone.smartDetails())


mark = meta("Meta", "200MP", "5TB", "100GB")
print(mark.attributes())


mark.metaOwner()
