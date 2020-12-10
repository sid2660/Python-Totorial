## Zip function
# user_id = ["user1","user2","user3"]
# names = ["Siddhartha","Mohit","Rohit"]
# last_name = ["Singh","Kumar","Verma"]
# num = [123,345,567]
## ("uaer1","Siddhartha"),("uaer2","Mohit")

# zip_func = list(zip(user_id,names,last_name,num))
# print(zip_func)


####

l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []

# l = [(1,2),(3,4),(5,6),(7,8)]
## * operator

# l1, l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))

### store max num
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)
