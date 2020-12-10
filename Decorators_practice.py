from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper


@print_function_data
def add(a,b):
    '''This function takes two numbers as argument and return there sum '''
    return a+b

print(add(4,5))

## Output 
## You are calling add function 
## This function takes two numbers as parameters and return their sum
## 9

