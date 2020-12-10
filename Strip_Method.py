#Strip Method
name = "    Siddhartha  "
dots = "..........."
print(name)
#lstrip() method (Remove spaces from the left side of strings)
print(name.lstrip(),dots)
#rsprit() method ( Remove spaces from the right side of strings)
print(name.rstrip(),dots)
#strip method 
print(name.strip(),dots)

#for remove all space we use 
#replace method
name = "    Sid dh ar tha  "
print(name)
#lstrip() method
print(name.lstrip()+dots)
#rsprit() method
print(name.rstrip()+dots)
#strip method
print(name.strip()+dots)
#replace method ( replace space to no space method)
print(name.replace(" ",""))

