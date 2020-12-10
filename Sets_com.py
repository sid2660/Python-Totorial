## Set Comprehension ---> Only one chapter

s = {k**2 for k in range(1,11)}
print(s)

names = ["Siddhartha","Mohit","Rohit"]
char = {name[0] for name in names}
print(char)