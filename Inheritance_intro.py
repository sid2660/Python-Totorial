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
        
phone = Phone("nokia","1100",1000)
smartphone = Smartphone("iphone","6",24000,"2GB","128GB","8 MP")
print(phone.full_name())
print(smartphone.full_name())
