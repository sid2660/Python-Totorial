## OBJECTIVES 
## WHAT IS CLASS
## HOW TO CREATE AN CLASS
## WHAT IS INIT METHOD
## WHAT ARE ATTRIBUTES, iNSTANCE VARIABLES
## HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        ## Instance varibles
        print("init method called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
        
p1 = Person("Siddhartha","Singh",24)

print(p1.first_name)                                                 
