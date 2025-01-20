listItems = ['Bihndi', 'Palak', 'Gobi', 'Chicken']

print("Enter a list of items")
items = input()

i = listItems.append(items)
print(f"Normal List: {listItems}\n")
rev1 = listItems[::-1]
print(f"Reverse List 1: {rev1}")
print(f"Reverse List 2: {rev1.copy()}")


for item in range(len(listItems)//2):
    listItems[item], listItems[len(listItems)-item-1] = listItems[len(listItems)-item-1], listItems[item]

print(f"Reverse List 3: {listItems}")