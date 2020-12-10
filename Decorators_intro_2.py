## Decorators - enhance the functionality of other function

## @ use for decorator

def decorator_func(any_func):
    def wrapper_func():
        print("This ia awesome function ")
        any_func()
    return wrapper_func

###
@decorator_func
def func1():
    print("This is function 1")
    
func1()

### 

# @decorator_func
# def func2():
#     print("This is function 2")
    
# func2()

### func1 = decorator_func(func1)
## func1()

