## Class methods 
## Difference b/w class methods and instance methods

class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    @classmethod
    def from_string(cls,string):
        first, last, age = string.split(",")  
        return cls(first,last,age)    
        
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of person class"
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above(self):
        return self.age>18
    
    
p1 = Person("Siddhartha","Singh",19)

p2 = Person("Sid","Singh",25)

p3 = Person.from_string("Siddhartha,Singh,20")

print(p3.full_name())
