## Class variable 
## circle
## area
## circumfrence

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def calc_circumfrence(self):
        return 2*Circle.pi*self.radius
    
c1 = Circle(4)
c2 = Circle(7)

print(c2.calc_circumfrence())