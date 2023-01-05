#Abstraction is used to hide internal details and show only functionalities.
#A class from which an object can not be created is called an abstract class.

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class circle(shape):
    def draw(self):
        print("Draw the circle")
class square(shape):
    def draw(self):
        print("Draw the square")
#s=shape()  --> this will show error because shape is abstract class
c=circle()
c.draw()
