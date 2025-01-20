listt = []

def friendsTable(table):
    i = 1
    while i<=10:
       listt.append(i*table)
       if i==7:
           listt.remove(listt[6])
           listt.append(77)
       i+=1
    print(listt)

def isCorrect(table):
    pass


friendsTable(10)