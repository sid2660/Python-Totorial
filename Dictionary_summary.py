## Dictionary Summary
## What is dictionary
## Unorderd collection of data.

d = {'name' : 'Siddhartha', 'age' : 20}

## Or

d1 = dict(name = 'Siddhartha', age = 20)

## Or 

d2 = {
    'name' : 'Siddhartha',
    'age' : 20,
    'fav_movies' : []
}

## How to access data from dictionary
## You cannot do like 
## d[0], because there is no orderd inside dictionary.
## Syntax
# print(d['name'])

## Add data inside empty dict

# empty_dict = {}
# empty_dict = ['key1'] = value1
# empty_dict = ['key2'] = value2
# print(empty_dict)

## Cheak existance of values inside dict
## Use in keyword to cheak for keys.

# if 'name' in d:

## How to iterate over dictionary 
## Most common method

# for key, value in d.items():
#     print(f'key is {key} and value is {value}')
    
## To print all keys
# for i in d:
#     print(i)

## To print all values
# for i in d.values():
#     print(i)
    
## Most common dict method. 
# get method 
# To access a key and check existance.

# print(d.get('names'))

## Q --> Why we use get
## A --> To get of rid of error

## Example

# print(d['names'])
# print(d.get('names'))

## To delete item
## Pop ----> Take one argument which is keyname

# popped = d.pop('name')
# print(popped)

## Popitem

# popped = d.popitem()
# print(popped)
# print(d)