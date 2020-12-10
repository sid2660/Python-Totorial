## Function with all parameters
## very important to understand

## PADK

## parameters
## *args
## default parameters
## **kwargs

def func(name = "unknown", age=19):
    print(name)
    print(age)
func("siddhartha",20)

## Order of Functions
def order(name,*args, last_name = 'Unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
order("Siddhartha", 1,2,3, a = 1, b =2)