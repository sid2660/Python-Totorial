## any, all function

# number1 = [2,4,6,8,10]
# number2 = [1,2,3,4,5,6]

# evens1 = []
# for num in number1:
#     evens1.append(num%2==0)
    
# # print(evens1)
# ## all function
# print(all([True,True,True,True,True])) ## if any of them is false then whole value is false


# ## list comprehension
# ## short form of coad

# print(all([num%2 == 0 for num in number1]))

# print(all([num%2 == 0 for num in number2]))

### Any function
# print(any([num%2 == 0 for num in number1])) 

# print(any([num%2 == 0 for num in number2]))## if any of them is true then the whole function is true


########### any and all practice ----> 161

def my_sum(*args):
    if all([(type(arg)== int or type(arg)== float) for arg in args]):
        total = 0
        for num in args:
            total +=num
        return total
    else:
        return "Wrong Input"
    
print(my_sum(1,2,3,4,9,2.3))