## instace method

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above(self):
        return self.age>18
    
    
p1 = Person("Siddhartha","Singh",19)

p2 = Person("Sid","Singh",25)

print(p1.full_name())

print(p1.is_above())


##
# l = [1,2,3]
# clear, pop
# l.clear()
# l.pop()
# list.clear(l)
# print(l)
# l.append(l,10)
# print(l)