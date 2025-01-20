import json

jStr =  '{"Shan":22, "Ali":30, "Hamza":43, "KAMAL":[34,23,2 ,5]}'
# print(jStr)
# print(jStr["KAMAL"])

convert1 = json.loads(jStr)
print(convert1["Ali"])

jStr2 = {"Ghar":8, "Kitchen":1, "BedRooms":6}

convert2 = json.dumps(jStr2)
print(convert2)

# json.load = ?
# json - sort_key in dumps?