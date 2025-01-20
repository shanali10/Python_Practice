import pickle

# cityList = ["Muzaffarabad", "Islamabad", "Karachi", "Lahore", "Peshawar"]
# fileObj = open("shaan.pkl", "wb")
# pickle.dump(cityList, fileObj)
# fileObj.close()

fileObj1 = open("shaan.pkl", "rb")
pick = pickle.load(fileObj1)
print(pick)
