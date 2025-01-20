print("How much apples do you have?")
app = int(input())
min = int(input("Enter Minimum Value\n"))
max = int(input("Enter Maximum Value\n"))

if app/min > 0 and app/max > 0:
    print(f"Minimum Students can get {app/min} apples "
          f"and Maximum Students can get {app/max} apples")

else:
    print("No of apples is not divisible")