## In keywords in set and for loop 
s = {'a', 'b', 'c'}

## In keywords to check if item is present or not in set

if 'a' in s:
    print('present')
else:
    print('not present')
    
## For loop 
for item in s:
    print(item)
    
s1 = {1,2,3,4}
s2 = {3,4,5,6}

## Union 
## Intersection

## Union set
## {1,2,3,4,5,6}
## for union use "Pipe" *************
# union_set = s1 s2
# print(union_set)

## Intersection
print(s1&s2)