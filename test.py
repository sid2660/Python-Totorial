
# #if n is odd print "Weird"
# # if n is even print "Not Weird"
# def odd_even(num):
#     if num % 2 == 0:
#         return "Not Weird"
#     else:
#         return "Weird"
# num = int(input())
# n = odd_even(num)
# print(n)


################################
# name,char = input("Enter comma seprated name and chrater : ").split(", ")
# print(f"length of your name is :  {len(name)}")
# print(f"Character of count : {name.lower().count(char.lower())}")

#############################


# Exercise one of three-------------------------------------------
# Sum of n natural number-----------------------------------------
# Ask a user for natural number(n)---------------------------------
# Print total from 1 to n.--------------------------------------

n  = int(input("Enter a natural number for the total sum : "))
total = 0
i = 1
while i<=n:
    total += i
    i += 1
    print(total)