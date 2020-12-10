import pdb # import pdb module
## module - python file contains useful classes and functions wrote
## by devloper


## According to wikipedia - Debugging is the process to finding and
#  resolving defects or problems within a computer program that prevent correct operaton
# of computer software or a system


## Why debugging
## 1.) Our program is not running and causing unexpected errors.
## 2.) Our program is working fine but not working the same way we want.


### Steps of Debugging 
## 1.) Set trace
## 2.) Execute code line by line
pdb.set_trace() ## l ---> find line , n ---> print, c ---> continue, q---> quit
name = input("Enter your name : ")
age = input("enter your age : ")
print(f"Hello {name} your age is {age}")
age2 = age +5
print(f"{name} you will be {age2} in next five years")
