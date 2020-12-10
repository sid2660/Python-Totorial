## Dictionary comprehension with if else
## d = {1:"odd",2:"even",3:"odd",4:"even"}

odd_even = {i:("even" if i%2 ==0 else "odd")for i in range(1,11)}
print(odd_even)

#### Single list print
for i,j in odd_even.items():
    print(f"{i} : {j}")
    

