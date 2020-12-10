## Generate lists with range function.
## Somthing more about pop method.
## Index method. 
## Pass list to a function.

# number = list(range(1,11)) ## Add list function in range function to get a ist of 1 to 10. 
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(number) ## Print list function include range function
# popped_item = number.pop()) ## Delete the last integer in the range function.
# print(number) 
# print(number.index(2)) ## By using index function get the number of the list of th range function. 
# print(number.index(1,3,11)) ## We can define where to start and where to stop.
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(number))