numbers = [1,2,3,4,5] ## tuples, string-----> iterables
squares = map(lambda a: a**2 , numbers) ## Iterator


### for numbers we need to create it iterable
iter_num = iter(numbers)
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))


#### map is a iterator so it`s don`t need to create iterable

print(next(squares))
print(next(squares))
print(next(squares))

### same thing in for loop
for i in numbers:
    print(i)