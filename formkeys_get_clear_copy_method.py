## Fromkeys
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age'], 'unknown')
# print(d)

## Get Method 

d = {'name' : 'Siddhartha', 'age' : 'unknown'}
# print(d['names'])
# print(d.get('names'))

# if 'name' in d:
#     print('present')
# else:
#     print('Not Present')

# if d.get('name'):
#     print('Present')
# else:
#     print('Not Present')

## Clear
# d.clear()
# print(d)

## Copy
d1 = d.copy()
print(d1.popitem())
print(d)
