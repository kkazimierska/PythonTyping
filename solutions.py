if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
    1 + 2

def greeting_notyping(name):
    return "Helo" + name

def greeting(name: str) -> str:
    return 'Hello ' + name

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def field(self):
        pass

class Square(Shape):
    def __init__(self, a: int):
        self.a = a

    def field(self):
        return self.a**2

s = Square(a=2)
field = s.field()
print(field)

class TheHobbit:
    def __len__(self):
        return 95022

class intLike(int):
    def __len__(self):
        return len(str(self))

number = intLike(456)
size = len(number)
print((size))

