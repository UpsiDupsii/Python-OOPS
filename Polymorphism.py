#'Polymorphism' word  is made two word "poly" and  "morph".'poly' means many and 'morph' means shape/forms.


#Method Overloading
#Same class --> Same function/method names --> but differnet (no.of) parameters

class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1): #by giving default parameter values, we can overcome method overloading
        return a+b+c
obj = A()
print(obj.sum(4,3,2)) #here value passed into the arguments will replace the value of parameters

#Method Over-riding
#Different class --> same method name --> different (no. of) parameters
class A():
    def display(self):
        print("This is class A")
class B(A):
    def display(self):
        print("This is class B")
        super(). display() # By using super(). keyword we can over come method over-riding
over = B()
over.display()


#'Polymorphism' word  is made two word "poly" and  "morph".'poly' means many and 'morph' means shape/forms.
#Polymorphism: Polmorphism is an Object Oriented Programming concept which means multiple forms or more than one form.
# (Eg: Human Behaviour: Person can be an employee and a customer)

''' Types of Polymorphism:
    1. Compile Time Polymorphism
        a> Method Over-Loading: 
            Same class having same method names but different parameters
    2. Runtime Polymorphism
        b> Method Over-Riding:
            Different class having same method names but differnt parameters
'''