# Define Fibonacci series
# 0 1 1 2 3 5 8 13 21 34
# for i in range(1,11):
#     print(i, end=(" ")) # 1 2 3 4 5 6 7 8 9 10
 
def fib_seq(n):
    a = 0 #First number
    b = 1 # Second Number
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a,b , end=(" "))
        for n in range(n-2):
            c = a+b
            a = b
            b = c
            print(b , end=(" , "))
n = int(input("Enter a number : "))
print(fib_seq(n))