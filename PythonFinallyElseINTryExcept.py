try:
    a = 100/2
    print(a)

except Exception as e:
    print(e)

else:
    print("Using else with except - it only runs if Exception does not occurs")

finally:
    print("Finally block runs at any cost")

print("Hello Shan")

