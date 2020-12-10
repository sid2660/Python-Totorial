#For Loop with range function
# for i in range(10):
#     print(f"Hello World : {i}")

#==============================================
# EXERCISE
#Sum of 1 to 10
# total = 0
# for i in range(1,11):
#     total += i
# print(total)
####
#Take user input.
# n = int(input("Enter a number : "))
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)
#================================================
#EXAMPLE 
# Practice for loop.
# Ask user a number like 1256
# Calculate Sum of digits ------> 1+2+5+6

#logic
#num =' 1256', length= 4
# int(num[0])-----> 1
# int(num[1])-----> 2
# int(num[2])-----> 5
# int(num[3])-----> 6
# i -------> 0 to 3

# total = 0
# num = input("Enter your number : ")
# for i in range (0, len(num)):
#     total += int(num[i])
# print(total)

##=============================================================
# EXAMPLE 
# Practice for loop
# Ask user name and count each character
# "Siddhartha Singh"
 # output
     # S : 1
     # i : 1
     # d : 2
     # d : 2
     # h : 2 
     # a : 2
     # r : 1
     # t : 1
     # h : 2 
     # a : 2
name = input("Enter your name : ")
temp = ""
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
