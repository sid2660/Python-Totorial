## Read file 
## open function
## read method
## seek method
## tell method
### readline method
## readlines method
## close method

f = open("Read_file.txt",'r') ## Open method

# print(f.readline(),end = "") ## Read line method is use for print single line 
# print(f.readline())


# print(f"cursor position - {f.tell()}") ## Tell method is use to find the position of cursor

# print(f.read()) ## Read method is use to read files
# print(f"cursor position - {f.tell()}")

# print("Before seek method")
# f.seek(0) ## seek method is use to start again reading the file from 0.
# print(f"cursor position - {f.tell()}")
# print("After seek method")

lines  = f.readlines() ## this method return a list
# print(lines)
for i in lines:
    print(i, end = "")

# print(f.read()) 
f.close() ## close method is use to close program