class Shan:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __repr__(self):
        return f"Details: {self.name}, {self.salary}"


s = Shan("Programmer", 100)
k = Shan("Electrical Engineer", 80)

print(s+k)
print(s)
