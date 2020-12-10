## Multiple Inheritance

class A:
    def class_a_method(self):
        return "I`m just a class of A Method"
    
    def hello(self):
        return "Hello from class A"
    
class B:
    def class_b_method(self):
        return "I`m just a class of B Method"
    
    def hello(self):
        return "Hello from class B"
    
    
class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
# print(help(C))
print(C.mro())
print(C.__mro__)