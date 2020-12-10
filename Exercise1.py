# #EXERCISE 1
# #THIS IS \\ DOUBLE backslash
# print("This is \\\\ Double backslash")
# # This is /\/\/\/\/\ montain
# print("thsi is /\\/\\/\\/\\/\\ mountain")
# #Print these \" \n \t \'
# print("He is awesome\\\"")
# print("He is \nawesome")
# print("He is \tawesome")
# print("he is \\' Awesome ") 
# Exercise 2
# num1=input("enter num 1: ")
# num2=input("enter num 2: ")
# num3=input("enter num 3: ")
# (int(num1)+int(num2)+int(num3)/3)
# num1,num2,num3= input("enter 3 num use commo :").split(",")
# print(f"Avrage of 3 numbers {int(num1)+int(num2)+int(num3)/3}")

# #Exercise 3
# name = input("Enter your name :")
# # revers=name[-1 : : -1]
# print(f"Revers name is {revers}")
# print in one line
# print(f"Revers name is {name[-1 : : -1]}")

#Exercise 3
#Take two comma seprated inputs from user
#1. User name example =Siddhartha
#2. A single character "S"
#output
#1. User name length
#2. Count the character thet user inputed.
# name,char = input("enter comma seprated name and character : ").split(", ")
# print(f"Length of your name is {len(name)}")
# # print(f"Character count : {name.count(char)}")##case sensitive
# ##2nd solution
# print(f"Character count : {name.lower().count(char.lower())}")##case insensitive

#EXERCISE 4
#Exercise Number gussing game
# make a varible , like winning_number and assing by number to it. 
# Ask user to guess a number
# if user guessed correctly then print "You Win !!!!"
#if user don`t guessed correctly then:
#If user guessed lower then actual number then print "Too Low"
#If user gussed higher then actual number then print "Too High"

# winning_number = 25
# user_input = int(input("Guess a number = "))
# if user_input == winning_number:
#     print("YOU WIN !!!!")
# else:
#     if user_input< winning_number:
#         print("TOO LOW !!!")
#     else:
#         print("TOO HIGH !!")

#EXERCISE 5
#Ask user`s name and age 
#if user name starts with ('a' or 'A') and age is 10 above.
#print "You can watch coco"
#Else print "Sorry, you cannot watch coco"
# name = input("Enter you name , Your name must be start with 'a' or 'A' : ")
# age = int(input("Enter your age: "))
# if (name[0] == "a" or name[0]=="A") and age >=10:
#     print("You can watch coco")
# else:
#     print("sorry , you cannot watch")

#-----------------------------------------------------------------
#Exercise 6
# Exercise one of three-------------------------------------------
# Sum of n natural number-----------------------------------------
# Ask a user for natural number(n)---------------------------------
# Print total from 1 to n.-----------------------------------------


# n = int(input("Enter a number : "))
# total = 0
# i = 1
# while i<=n:
#     total = total+ i
#     i += 1
#     print(total)

#===================================================================================
# Exercise 7
# Problem
# Ask  user to input a number containig more than one digit.
# Example - 1256
# Calculate 1+2+5+6 and print
# Algorithm - (method to solve problem in human language)
# Ask input i string , i.e don`t change sting to int.
# Example - "1 2 5 6"
# Pick string chracter one by one and change to int.
# int(example[0]) + int(example[1])_______ go upto len(example).

# # 1256 # length = 4, last index = 3
# number = input("Enter a number more than one chr. : ")

# total = 0
# i = 0
# while i< len(number):
#     total += int(number[i])
#     i+= 1
# print(total)

#=================================================================

#EXERCISE 8
#problem
# Ask user for name 
# Example - Siddhartha
# print count of each words:
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
# sol
#----------------------------------------------------------------------------

# name = input("Enter your name: ")
# Siddhartha  , len 10-1=9

#name.count("S") , name.count(name[0])
#name.count("i") , name.count(name[1])
#name.count("d") , name.count(name[2])
#name.count("d") , name.count(name[3])
#name.count("h") , name.count(name[4])
#name.count("a") , name.count(name[5])
#name.count("r") , name.count(name[6])
#name.count("t") , name.count(name[7])
#name.count("h") , name.count(name[8])
#name.count("a") , name.count(name[9])

#output
# s : 1
# i : 1
# d : 2
# d : 2
# h : 2
# a : 2
# r : 1
# t : 1
# h : 2
# a : 2
# temp_var = ""
# i = 0
# while i < len(name):
#     if name [i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i += 1

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
# name = input("Enter your name : ")
# temp = ""
# for i in range (0,len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp += name[i]
###

#########
#Define a Function which takes two numbers as a input and return grater of two numbers
# print("Function Define the grater number")
# def grt_num(a,b):
#      if a>b:
#           return a 
#      return b
# a,b = input("Enter two Number space seprated : ").split(" ")
# t = int(grt_num(a,b))
# print(t)

###---------------------------------------------------------------------------####
### EXERCISE
## Define a function which will take a list containing number as input.
## And return list containing square of every element.

## Example
# # numbers = [1, 2, 3, 4]
# # square_list(number) = [1,4,9,16]



# def square_list(l):
#      square = []
#      for i in l:
#           square.append(i**2)
#      return square
# number = (range(0, 5))
# print(square_list(number))

######------------------------------------------------------------------------###
# Define a function which will take list as a argument and this function will 
## return  a reversed list.
# Examples.
# [ 1, 2, 3, 4] ----> [4, 3, 2, 1]
# ['Word1', 'Word2'] ----> ['Word2', 'Word1']

## Note you simply do this with reverse method or[ : : -1]
## But try to do this with the help of append and pop method. 

# def reverse_list(l):
#      return l[::-1] ## return l[::-1]

# def reverse_list(l):
#      r_list= []
#      for i in range (len(l)):  ##range(1, len(l)+1)   This can also use.
#           popped_item = l.pop()
#           r_list.append(popped_item)
#      return r_list
          

# number = [1, 2, 3, 4]
# words = ['Word1', 'Word2']
# print(reverse_list(number))
# print(reverse_list(words))

#####=----------------------------------------------------------------#####
## Define a function that take list of words as argument and return list with reverse of every element in that list.

## Example
## ['abc' 'tuv' 'xyz'] ------> ['cba' 'vut' 'zyx' ]
# def reverse_elements(l):
#      elements = []
#      for i in l:
#           elements.append(i[::-1])
#      return elements

# words = ['abc', 'tuv', 'xyz']
# print(reverse_elements(words))

#####=-------------------------------------------------------#####

# Filter odd even 
# Define a function
# input
# list -----> [1, 2, 3, 4, 5, 6, 7]
# output -----> [[1, 3, 5, 7], [2, 4, 6]]

# def fil_odd_even(l):
#      odd_num = []
#      even_num = []
#      for i in l:
#           if i % 2==0:
#                even_num.append(i)
#           else:
#                odd_num.append(i)
#      output = [odd_num, even_num]
#      return output

# number = [1, 2, 3, 4, 5, 6, 7]
# print(fil_odd_even(number))
     
####============================================-----------------------#####

#Common elements finder function 
# Define a function which take 2list as input and return a list
# Which contains common elements of both list

## Example 
# # input -----> [1, 2, 5, 8], [1, 2, 7, 6]
# # Output ---> [1, 2]

# def comm_fun  (l1 , l2):
#      output = []
#      for i in l1:
#           if i in l2:
#                output.append(i)
#      return output
# print(comm_fun([1, 2, 5, 8], [1, 2, 7, 6]))
          
#####===================================------------------------===####

## List function 
## [1, 2, 3, [1, 2], [3, 4]] ---> Input
## 2
## find the number of list`s inside list. 
## Type() function

# def sub_list(l):
#      count = 0
#      for i in l:
#           if type(i) == list:
#                count += 1
#      return count
# print(sub_list([1, 2, 3, [1, 2],[2], [3, 4]]))

#################------------------------------------------########################

##Exercise 
## Define a function that takes a number(n)
## Return a dictionary containing cube of numbers from 1 to n.

## Example 
## Cube_finder(3)
## {1:1, 2:8, 3:27}

## Solution 

# def cube_finder(n):
#      cube = {}
#      for i in range (1, n+1):
#           cube[i] = i**3
#      return cube
# print(cube_finder(10))


################################-----------------------------------#####################
## Define a function that take list of strings 
## List contaning reverse of every string

## NOTE- Use list comprehension because we alredy did this 

### Exercise
## Using normal method 
## Example 
##  l = ['abc', 'tuv', 'xyz']
## reverse_string(l) ----> ['cab', 'vut', 'zyx']

## Solution

# def reverse_string(l):
#      return [name[::-1] for name in l]

# print(reverse_string(['abc', 'tuv', 'xyz']))

##2

# def reverse_str(l):
#      new_list = []
#      for name in l:
#           new_list.append(name[::-1])
#      return new_list
# print(reverse_str(['abc', 'tuv', 'xyz']))

####### Exercise -----> Video 132 - 133
##  num to string
## define a function

##example
## input -----> [True,False, [1,2,3], 1,1.0,3]
## output ----> ["1", "1.0", "3"]


# def num_to_str(l):
#      return [str(i) for i in l if (type(i) == int or type(i) == float)]
# print(num_to_str([True,False, [1,2,3], 1,1.0,3]))
# print(type(num_to_str))




####### Exercise ---> Video 143- 144

## define a function 
## Input
## num, iterable(tuple, list)containing numbers as args

## Example 
## num = [1,2,3]
## to_power(3,*nums)

##Output
## list-----> [1**3,8,27]

## if user didn`t pass any args then give a user a message "Hey you did`t pass args"

## else
## return list

## NOTE - Use list comprehension


# def to_power(num, *args):
#      if args:
#           return [i**num for i in args]
#      else:
#           return "You didn`t pass args"
     
# nums = [2,3,4]
# print(to_power(3,*nums))


############ Exercise ---> 147,148


## Function 
## list, reverse_str = True
## list

# def func(l, **kwargs):
#      if kwargs.get("reverse_str") == True:
#           return [name[::-1].title() for name in l]
#      else:
#           return [name.title() for name in l]
# names = ["Siddhartha","Mohit"]
# print(func(names))
# print(func(names,reverse_str = True))



######### Exercise ----> 173-174

## exercise
# import time 

# t1 = time.time()
# print('Tis is line one')
# x = 5
# if x == 5:
#      print('x is equal to 5')
# print('this is line two')

# t2 = time.time()
# print(t2-t1)


#@calculate_time
#def func():
#    print('This is function)

#func()
## This function took 3sec to run

## sol
# from functools import wraps
# import time
# def cal_time(function):
#      @wraps(function)
#      def wrapper(*args, **kwargs):
#           print(f"Executing .....{function.__name__}")
#           t1 = time.time()
#           return_val = function(*args,**kwargs)
#           t2 = time.time()
#           total_time = t2-t1
#           print(f"this function took {total_time}")
#           return return_val
#      return wrapper

# @cal_time
# def square_finder(n):
#      return [i**2 for i in range(1,n+1)]

# print(square_finder(1000))



###### Exercise -----> 179-180

## define generator function
## take one number as argument
## generate a sequence of even numbers from 1 to that numbers
## 5 ---> 2,4
## 7 ---> 2,4,6


# def even_gen(n):
#      for num in range(1,n+1):
#           if num % 2 == 0:
#                yield(num)
               
# even_nums = even_gen(20)
# for num in even_nums: ## if i use this i can`t print this loop many times
#      print(num)
     
# for num in even_gen(20): ##  if i use this then i print this loop many times 
#      print(num)i


############## Exercise ------> 185,186
## Create a laptop class with attributes like brand name , model name , price
## create two objects / instance of your laptop

# class Laptop:
#      def __init__(self,brand_name,model_name,price):
#           self.brand = brand_name
#           self.model = model_name
#           self.price = price
#           self.pc_name = brand_name+ " "+model_name



# pc1= Laptop("HP","HPP9860",24599)


# pc2 = Laptop("Apple","Mackbook",95000)

# print(pc1.pc_name)
# print(pc2.pc_name)




########### Exercise -----> 188-189

# class Laptop:
#      def __init__(self,brand_name,model_name,price):
#           self.brand = brand_name
#           self.model = model_name
#           self.price = price
#           self.pc_name = brand_name+ " "+model_name


#      def apply_discount(self,num):
#           off_price = (num/100)*self.price
#           return self.price - off_price

# num = int(input("Enter discout price : "))
# pc1= Laptop("HP","HPP9860",24599)
# print(pc1.apply_discount(num))


####### Exercise ---->192-193

# class Person:
#      count_instance = 0
#      def __init__(self,first_name,last_name,age):
#           Person.count_instance += 1
#           self.first_name = first_name
#           self.last_name = last_name
#           self.age = age
          

# p1 = Person("Siddhartha","Singh",20)
# pc2 = Person("Siddhartha","Singh",20)
# p3  = Person("Siddhartha","Singh",20)

# print(Person.count_instance)


###### Exercise - 210
# def divide(a,b):
#      try:
#           return a/b
#      except ZeroDivisionError:
#           print("You can`t divide a num by zero")
#      except TypeError:
#           print("Numbers must be int or floats")
#      except:
#           print("Unexpected error")
          
# print(divide(10,"2"))

######


################ Exercise ----> 217-218

# with open("Read_file.txt","r") as rf:
#      with open("Read_file2.txt","a") as wf:
#           for line in rf.readlines():
#                name,salary = line.split(",")
#                wf.write(f"{name} your salary is {salary}")
               
               
               
               
######## 
#### 


########### Exercise ----> 219 - 220
# with open("exercise.html","r") as rf:
#      with open("output.txt","a") as wf:
#           for line in rf.readlines():
#                if "<a href=" in line:
#                     pos = line.find("<a href=")
#                     first_quote = line.find('\"',pos)
#                     second_quote = line.find('\"',first_quote+1)
#                     url = line[first_quote+1:second_quote]
#                     wf.write(url+'\n')

                    
                    