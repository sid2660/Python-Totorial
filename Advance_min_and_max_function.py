## Advance min() and max() function

# numbers = [1,2,4,5,7]
# print(max(numbers))
def func(item):
    return len(item)

names = ["Harshit","Mohit","ab"]
print(max(names,key = func))
print(min(names,key = func))


###Simple way
print(max(names,key = lambda item : len(item)))
##
students = {
    "harshit" : {"score" : 90, "age" : 24},
    "mohit" : {"score" : 95, "age" : 19},
    "rohit" : {"score" : 76, "age" : 23}
}

print(max(students, key = lambda item : students[item]["score"]))

###
students2 = [
    {"name":"harshit","score" : 90, "age" : 24},
    {"name":"mohit","score" : 75, "age" : 19},
    {"name":"rohit","score" : 76, "age" : 23}
]

print(max(students2, key = lambda item: item.get("age"))["name"])