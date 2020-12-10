def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,2,3,4))

nums = [2,3,4]##,(2,3,4)
print(multiply_nums(*nums))## tuples unpacking