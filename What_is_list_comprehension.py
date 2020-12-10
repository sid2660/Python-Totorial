## What is list comprehension.
## List comprehension
## With the help of list comprehension we can create of list in one line.

## Create a list of squares from 1 to 10

# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# squares = [i**2 for i in range(1,11)]
# print(squares)


# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)   

# new_negative = [-i for i in range(1,11)]
# print(new_negative)

names = ['Harshit', 'Mohit', 'Rohit']
## new_list = ['H', 'M', 'R']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)


names2 = [name[0] for name in names]
print(names2)