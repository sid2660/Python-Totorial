from functools import wraps

def decorator_func(any_func):
    @wraps(any_func) ## (without this function add doc is showing in rapper func)
    def wrapper_func(*args, **kwargs):
        """ This is wrapper function"""
        print("This ia awesome function ")
        return any_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def add(a,b):
    """This is add func """
    return a + b
print(add(2,3))

print(add.__doc__)
print(add.__name__)
