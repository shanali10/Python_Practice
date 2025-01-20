def nextPalindrome(n):
    n = n + 1
    while not isPalindrome(n):
        n = n + 1
    return n


def isPalindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    print("Enter the test times")
    test = int(input())
    lis = []
    numbers = None
    for i in range(test):
        print("Enter the number")
        numbers = int(input())
        lis.append(numbers)
    newLis = []
    print(f"Your Previous List: {lis}")
    for i in lis:
        if i > 10:
            a = nextPalindrome(i)
            newLis.append(a)
        else:
            newLis.append(i)
    print(f"Your New List: {newLis}")
