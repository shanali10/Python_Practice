listt = ["Shan", "Rock", "Alex", "Buddha"]

# without Join Function
for item in listt:
    print(f"{item} or", end= " ")


# with Join Function

j = " and ".join(listt)
print("\n"+j)