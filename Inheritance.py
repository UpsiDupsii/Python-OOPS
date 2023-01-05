#In inheritance, a new class called derived class can be created to inherit features of an existing class called base class.
#Base class is also known as super class or parent class, Derived class is also know as sub class or child class.
#Inheritance concept provide the re-usability of code.
class Parent:
    def __init__(self):
        print("This is the Parent class")
    
    def addition(self,a,b):
        self.a = a
        self.b = b 
        self.sum = self.a + self.b
        print("Addition is: ",self.sum)
    def subtraction(self):
        self.sub = self.a - self.b 
        print("Subtraction is: ",self.sub)
        
class Child(Parent):
    def __init__(self):
        print("This is a Child class")
        #By using super(). function, __init__() from parent class can be called
        super().__init__()
    def multiply(self):
        self.multi = self.a * self.b 
        print("Multiplication is: ",self.multi)
    def division(self):
        self.div = self.a / self.b 
        print("Division is: ",self.div)
        
inherit = Child()
inherit.addition(10,4)
inherit.subtraction()
inherit.multiply()
inherit.division()