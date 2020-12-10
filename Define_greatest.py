# Define greatest number between three numbers
def grt_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and  b>c:
        return b
    elif c>a and c>b:
        return c
a,b,c = input("Enter three numbers space seprated : ").split(" ")
t = int(grt_num(a,b,c))
print(t)