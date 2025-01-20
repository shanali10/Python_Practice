# Dictionary is Key-value pairs

dic = {"Shan": 333, "Ali": 444, "Aryan": 555, "Malik":666, "Adam":"Fail",
       "Arslan": {"Urdu": 54, "English": 75, "Mathematics": 83} }

dic["Ahmad"] = "Topper"
dic["Kainat"] = "Proctor"


print(type(dic))
print(dic)

print(dic["Shan"])
print(dic["Adam"])

print(dic["Arslan"])
print(dic["Arslan"]["Mathematics"])

del dic["Kainat"]
print(dic)

print(dic.keys())
print(dic.items())