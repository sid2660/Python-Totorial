# Data Structure
# List----> This chapter
# You can store anything in list int, float, string.

# number = [1,2,3,4,5,6]
# print(number)
# word = ["words1", "words2"]
# print(word)
# mixed = [1,2,3,4, "word1", "word2" , 2.3]
# print(mixed)

##------------------------------------ Add Data to List ----------------->>

# How to add items to our list. 
# Most common things that you can do with your list and most important.

# fruits = ["graps", "apple"]
# fruits.append(input("name of fruits : ").split(" "))
# print(fruits)

##------------------------------------------>
## More Methods to add data. 
# Some more methods to add data in our list,
# Insert method,
# How to join(Concatenate ) two list ,
# Extend Method,
# Difference b/w append and extend method,

# fruits1 = ["mango", "apple"]
# fruits1.insert(2, "grapes")
# # print(fruits1)
# fruits2 = ["banana", "grapes"]
# fruits = fruits1 + fruits2
# print(fruits)
####Take input from user
# fruits1 = input("Enter fruits name space seprated: ").split(" ")
# fruits2 = input("Enter another two names space  seprated : ").split(" ")
# fruits = fruits1 + fruits2
# print(fruits)

###
# fruits1 = ["mango", "apple"]
# fruits2 = ["banana", "grapes"]
# # fruits1.insert(fruits2)
# fruits1.append(fruits2)
# print(fruits1)


########--------------------------------------------------------------------->
## Delete Data from list
# Common method to delete data from list
# fruits = ["Orange", "Apple", "Grapes", "Mango", "Kiwi"]
##Pop Method ( This method is use to delete data from the list)
# fruits.pop(0)## If no argument pass then it delete the last element.
## Del method (This is also use for delete data from the list)
# del fruits[1] ### Pass argument without agrument this is not able to delete any data.
## Remove method (This is also able to delete data from the list)
# fruits.remove(input("Enter the name of fruit which you want delete : "))## Enter the name of the string thats you want to delete.
# print(fruits)

####----------------------------------------------------------------------->
## In keyword with List

##
# fruits = ["Orange", "Apple", "Grapes", "Mango", "Kiwi"]
# f = input("Enter the nane of fruit : ")
# if f in fruits:
#     print(f, " is present")
# else:
#     print("Not present")


###---------------------------------------------------------------------->
## Some more list methods.
## Count
## Sort method 
## Sorted function
## reverse
## clear
## copy

# fruits= ["Orange", "Apple", "Pear", "Banana", "Kiwi", "Apple", "Banana"]
# print(fruits.count("Apple")) ## This method is use to count the number of fruits in the list.

# fruits.sort() ### This method is use to sort the number of fruits in the list or any other list to arrenge in list. 
# print(fruits)

numbers = [3, 1, 9, 5, 10]
# print(sorted(numbers)) ## This function sorted the list but not change the orignal list.

# numbers.clear() #### This method is use to clear the list.
# print(numbers)

num_copy = numbers.copy()  ### This method is use to copy the list in another function.
print(num_copy)