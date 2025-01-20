import os

def prettySoldier(path, file, format):
    os.chdir(path)
    i = 1
    file1 = os.listdir(file)
    file2 = open(file)
    file3 = file2.read().split("\n")

    for file in file1:
        if file not in file1:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(f"{file}{format}")
            i+=1


prettySoldier(r"C:\Users\Administrator\OneDrive\Desktop\File Test",
              r"F:\Python Programs\soldier.txt", ".txt")

