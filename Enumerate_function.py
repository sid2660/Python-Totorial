### We use enumerate function with for loop to track position of our
## item in iterable



## How we can do this without enumerate function

names = ["Siddhartha","Harshit","Rohit","Mohit"]
## 0 ---> Sidd
## 1---> Har

# pos = 0 #### Position of string
# for name in names:
    # print(f"{pos}----> {name}")
    # pos += 1
    
## with enumerate function

# for pos, name in enumerate(names):
    # print(f"{pos}----> {name}")




### Define a function that take two arguments
## 1.) List contaning string
## 2.) String that want to find in your list
## and this function will return the index of string in your list and 
## if string is not present then return -1

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos  ## Thsi can also used (f"position of string ----> {pos}")
    return -1

print(find_pos(names,"Rohit"))