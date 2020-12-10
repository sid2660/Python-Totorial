class Laptop:
    discount_percent = 10
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.pc_name = brand_name+ " "+model_name


    def apply_discount(self):
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price

# Laptop.discount_percent=0
# num = int(input("Enter discout price : "))
pc1= Laptop("HP","HPP9860",24599)
pc2= Laptop("Apple","macbook",250000)

# print(pc1.apply_discount())

pc2.discount_percent = 50
print(pc2.__dict__)
print(pc2.apply_discount())