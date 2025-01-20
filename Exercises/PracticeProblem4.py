def nextPalindrome(n):
    n = n+1
    while not isPalindrome(n):
        n = n+1

    return n

def isPalindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    print("How many times you want the number to Palindrome?")
    times = int(input())
    lis = []
    for i in range(times):
        print("Enter the number to find its next Palindrome")
        pNumber = int(input())
        lis.append(pNumber)

    for i in range(times):
        print(f"The Palindrome of {lis[i]} is {nextPalindrome(lis[i])}")







