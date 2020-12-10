## In this video we will talk about 
## Encapsulation
## Abstraction
## Some special naming convention
## Name mangling

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = price
        
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}.....")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def send_message(self):
        pass ## twilio
    
phone = Phone("nokia","1100",1000)
# print(phone._price)    
# phone._price = -1000
print(phone._price)
phone._Phone__price = -1000
print(phone._Phone__price)
print(phone.__dict__)
## _name --> Convention of private names
## __name__ --->  dunder

l = [3,4,5,2,1]
l.sort() ##tim sort
print(l)
