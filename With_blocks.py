# f = open("Read_file.txt")
# f.read()
# f.close()

## with block
## Context manager
with open("Read_file.txt") as f:
    data = f.read()
    print(data)
    
print(f.closed)## this is use to check its close or not