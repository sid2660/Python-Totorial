## Python Custom Exceptions
## Q - Why custom exceptions?
## A- To increase the readability of code.

## example
class NameTooshort(ValueError):
    pass

def validate(name):
    if len(name)  < 8:
        raise NameTooshort("Name is too short")
    
username = input("Enter your name : ")
validate(username)
print(f"hello {username}")
