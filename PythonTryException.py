print("Enter 1st Number for division")
num1 = int(input())
print("Enter 2nd Number for division")
num2 = int(input())

try:
    print("Result =", num1/num2)

except Exception as e:
    print(e)

print("You handled Exception Successfully!")
