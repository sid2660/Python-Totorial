## Intro to * args

## Make flexible functions
## * operator
## * args

### We can`t add more than two int in this functon
def total(a,b):
    return a + b
# print(total(1,2,3,4))

## print all int
def all_total(*args):
    print(args)
    print(type(args))
    
all_total(1,2,3,4,5,6)

## Add more than one int
def a_total(*args):
    #(1,2,3,4,5,6)
    total = 0
    for num in args:
        total += num
    return total
print(a_total(1,2,3,4,5,6))