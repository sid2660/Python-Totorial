## Map function 

numbers = [1,2,3,4]

def square(a):
    return a**2

## map fun
squares = list(map(square,numbers))
print(squares)

### Simple 

squares2 = list(map(lambda a : a**2,numbers))
print(squares2)

## use list comprehension
square_new = [i**2 for i in numbers]
print(square_new)

## without map function

new_list =[]
for num in numbers:
    new_list.append(square(num))
    
print(new_list)

### find the len of strings
names = ["abc","bcdd","dwdef"]
length = map(len,names) ## if we use list fun() then run more than one time
for i in length:
    print(i)
     