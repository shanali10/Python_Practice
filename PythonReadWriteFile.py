f = open("shan2.txt", "r+")
f.write("Hello Bro, How are You")

f.write("\n Now Read and Writing file")
reading = f.read()

f.write("\n Hello i Am now using both read write file system")
print(reading)
f.close()


