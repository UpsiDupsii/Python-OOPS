# Class is a BLUEPRINT of an Obect
# Class is a collection of Data and Methods

class Students:
    def __init__(self,boys,girls):
        self.boys = boys
        self.girls = girls
        
    def class_strength(self):
        self.total = self.boys + self.girls
        print ("Total strength of class is",self.total)

classTotal = Students(12,12)
classTotal.class_strength()