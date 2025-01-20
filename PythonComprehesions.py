print("Which Comprehesion do you Want to do?\n"
      "Press 1 for List Comprehesion\n "
      "Press 2 for Dictionary Comprehesion\n"
      "Press 3 for Set Comprehesion")

comInp = int(input())



i = 0
while (i==0):



      if comInp == 1:
            print("How many items do you want to enter?")
            itemss = int(input())
            lst = [i for i in range(1, itemss + 1) if i%10 == 0]
            print(lst)
      elif comInp == 2:
            print("How many items do you want to enter?")
            itemss = int(input())
            print("Enter the name of the items")
            it = input()
            dic = {i:f"{it} {i}" for i in range(itemss)}
            print(dic)

      elif comInp == 3:
            print("Enter the name of the items")
            it = input()
            st = {i for i in [it]}
            print(st)

      else:
            print("Please Enter the Correct Option")

      i+=1
