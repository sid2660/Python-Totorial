# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("Opps you are passing wrong data type to function")


# print(add("2","3"))




##### Example

## Raise errors example1 
## Not Implemented Error 
## Abstract Method

# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def sound(self):
#         raise NotImplementedError("You have to define this method in subclass")
    
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
        
#     def sound(self):
#         return "Bhow Bhow"    
        
# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
        
#     def sound(self):
#         return "Meao meao"    
    
# doggy = Dog("Bonny","Pug")
# print(doggy.sound())



####### Example 2
class Mobile:
    def __init__(self,name):
        self.name = name
        
class MobileStore:
    def __init__(self):
        self.mobiles = []
        
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New mobile should be object of Mobile class")
        
        
oneplus = Mobile("One plus 6")
samsung = "Samsung galaxy s9"
mobostore = MobileStore()
# print(mobostore.mobiles)
mobostore.add_mobile(oneplus)
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)


