print("Enter your age or Year of birth")
age = int(input())


if age >= 1 and age < 100:
    ageSubtraction = 2022 - age
    age100 = ageSubtraction + 100
    print(f"You will be hundred Years old in {age100}")

    print("Enter the Year if you want to know your age in that year")
    year = int(input())
    print(f"You will be {year - ageSubtraction} Years Old in {year}")

elif age >= 1922 and age <= 2022:
    ageYear = age + 100
    print(f"You will be hundred years old in {ageYear}")

    print("Enter the Year if you want to know your age in that year")
    year = int(input())
    print(f"You will be {year - age} Years Old in {year}")

elif age > 2022:
    print("You are not born yet! Don't try to be over smart")

elif age < 1922 and age > 100:
    print("You should be dead now!")

elif age < 1:
    print("Something went wrong!")


