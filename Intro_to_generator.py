## Create your first generator with generator function
# 1.) generator function

## 10, 1 to 10

def num(n):
    for i in range(1,n+1):
        yield i
        
numbers = num(10)

for num in numbers:
    print(num) ## its iterable 