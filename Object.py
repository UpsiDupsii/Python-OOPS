# Object is INSTANCE of the Class, Object is an entity that has some state and behaviour
#We can access the class data with the help of object(instance) of the class

class Employee:
    def __init__(self,id,Salary,Role):
        self.id = id
        self.Salary = Salary
        self.Role = Role 
        
    def showData(self):
        print("Employee ID: ",self.id)
        print("Emploree Salary: ",self.Salary)
        print("Employee Role: ",self.Role)

John = Employee(2738,'$500,000','Data Scientist')
John.showData()
print("-------------------")
Doe = Employee(4937,'$499,000','Software Testing')
Doe.showData()
