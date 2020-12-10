## map
# def square(a):
#     return a**2

l = [1,2,3,4]
print(list(map(lambda a: a**2,l)))

### create own map function

def my_map(func, i):
    new_list = []
    for item in i:
        new_list.append(func(item))
    return new_list


print(my_map(lambda a: a**3 , l))

### use list com
def my_map2(func, l):
    return [func(item) for item in l]
print(my_map2(lambda a: a**3 , l))