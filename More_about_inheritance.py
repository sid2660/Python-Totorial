## We derive more than one class from base class
## multilevel inheritance
## Method resolution order
## method overriding
## isinstance(), issubclass()


class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
        
    def full_name(self):
        return f"{self.brand} {self.model}"
        
    def make_a_call(self,number):
        return f"Calling {number}....."
    
 
class Smartphone(Phone): ## derived class
    def __init__(self,brand,model,price,ram,rom,cam):
        # Phone.__init__(self,brand,model,price)
        super().__init__(brand,model,price)
        self.ram = ram
        self.rom = rom
        self.cam = cam
        
    def full_name(self):
        return f"{self.brand} {self.model} price is  {self._price}"

class Flagshipphone(Smartphone):
    def __init__(self,brand,model,price,ram,rom,cam,battery):
        super().__init__(brand,model,price,ram,rom,cam)
        self.battery = battery
        
    def full_name(self):
        return f"{self.brand} {self.model} price is  {self._price} and cam is {self.cam}"    
        
        
        
        
        
        
phone = Phone("nokia","1100",1000)
smartphone = Smartphone("iphone","6",24000,"2GB","128GB","8 MP")
flagship = Flagshipphone("iphone","7",42000,"2GB","128GB","12 MP","3200 Mah")

print(phone.full_name())
print(smartphone.full_name())
print(flagship.full_name())

## Method Resolution Order
# print(help(smartphone))


#####  Isinstance
iphone6 = Smartphone("iphone","6",24000,"2GB","128GB","8 MP")
print(isinstance(iphone6,Smartphone))

### Issubclass
print(issubclass(Smartphone,Phone))
