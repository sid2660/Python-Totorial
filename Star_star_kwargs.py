## Kwargs (keyword argument)
## **Kwargs (double star operator)

## kwargs as a oprater
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
func(first_name = "Siddhartha", Last_name = "Singh")

###
def func2(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func2(first_name = "Siddhartha", Last_name = "Singh")

### Dictionary Unpacking
def func3(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
        
d = {"name":"sid","age":19}
func3(**d)