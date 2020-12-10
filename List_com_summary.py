### list Comprehension
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

### 
square1 = [i**2 for i in range(1,11)]
print(square1)
 ##
even_num = [i for i in range(1,11) if i%2 == 0]
print(even_num)

## 
odd_num = [i for i in range(1,11) if i%2 != 0]
print(odd_num)

## if else 
## odd (-i), even (i*2)

even_odd = [i*2 if i%2 == 0 else -i for i in range(1,11)]
print(even_odd)

## list inside lists
l1 = [[i for i in range(1,4)] for j in range(3) ]
print(l1)