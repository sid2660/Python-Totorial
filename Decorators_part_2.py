def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print("This ia awesome function ")
        return any_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def func(a):
    print(f"This is function with argument {a}")
    
func(5)


@decorator_func
def add(a,b):
    return a + b
print(add(2,3))