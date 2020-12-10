## filter function

def is_even(a):
    return a%2 == 0

numbers = [3,4,5,6,7,8,9,10]

evens = tuple(filter(is_even, numbers))
print(evens)

## simple

even1 = tuple(filter(lambda a : a%2 == 0,numbers))
print(even1)
# for i in even1:
#     print(i)

### list com
new_even = [i for i in numbers if i%2 == 0]
print(new_even)