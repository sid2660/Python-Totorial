def is_even(a):
    return a%2 == 0
print(is_even(5))


### simple
is_even2 = lambda a : a%2==0
print(is_even2(4))

###
def last_char(s):
    return s[-1]

## simple
last_char1 = lambda s : s[-1]
print(last_char1("siddhartha"))

## lambda with if, else
def func(s):
    if len(s) > 5:
        return True
    return False


func2 = lambda s : True if len(s) > 5 else False
print(func2("Siddhartha"))
## simple 
func3 = lambda s: len(s) > 5
print(func3("Siddhartha"))