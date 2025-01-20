import abc
from abc import ABC, abstractmethod

class Abs(ABC):
    @abstractmethod
    def name(self):
        return 0

class base(Abs):
    a = 55
    def name(self):
        return 10 * 10


ob = base()
print(ob.name())

# hello this is shan ali mughal and this is my laptop that's it
