## Will disscus three problems in existing 
## then we will solve them using getter, setter decorator

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price =0
        # self.complete_specification = f"{self.brand} {self.model} and price is {self._price}"
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self._price}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}.....")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
phone = Phone("Nokia","1100", 1000)
print(phone.brand)
print(phone.model)
phone.price = -500
print(phone.price)
print(phone.complete_specification) 
