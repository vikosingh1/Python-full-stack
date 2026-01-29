# abstract method
from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class dog (animal):
    def sound(self):
        print("bhaw")


class cat(animal):
    def sound(self):
        print("meow")


obj1 = dog()
obj1.sound()
obj2 = cat()
obj2.sound()
