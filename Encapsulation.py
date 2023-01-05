#Encapsulation: Encapsulation is a process of binding (wrapping) of data into a Single Unit
#In encapsulation methodology we can restrict access to methods and variables.
#To prevent the data access of the class from out side or same class, is known as encapsulation.
#In python,we denote private attributes using prefix underscore(single(_) or double(__)).
class Payment():
    def __init__(self,price):
        self.__final_price = price + price*0.05
        
    def get_final_price(self):
        return self.__final_price 
    
    def set_final_price(self,discount):
        self.__final_price = self.__final_price - (self.__final_price * (discount/100))    


Book = Payment(100)

Book.set_final_price(10)
print(Book.get_final_price())