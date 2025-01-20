def fibonnaci_recursive(n):
    if n==1 or n==2:
        return (n-1)
    else:
        return fibonnaci_recursive(n-1) + fibonnaci_recursive(n-2)

# def fibonnaci_iterative(n):
#
#     if n==1 or n==2:
#         return (n-1)
#     else:
#         return (n-1) + (n-2)



number = int(input("Enter any Number for Fibonnaci Series Recursive\n"))
print("Ans = ", fibonnaci_recursive(number))
