# Dictionaries intro
# Q - Why we use dictionaries?
# A - Because o limitations of list , lists are not enough to repesent.
# Real data 

## Example

user = ['Siddhartha', 19, ['Coco,' 'Kimi no vo wa'], ['Awaking', 'Fairy tail']]
## This list conatins user name , age , fav movies , fav tunes.
## You can do this but this is not a good way to do this.

# Q - What is dictionaries?
# A - Unorderd collections of data in key : value pairs.

# How to create dictionaries.

user = {'name' : 'Siddhartha', 'age' : 19}
# print(user)
# print(type(user))

# Second method to create dictionary
user1 = dict(name = 'Siddhartha', age = 19)
# print(user1)

# How to access data from dictionary 
# NOTE - Ther is no indexing because of unorderd collections of data.
# print(user['name'])
# print(user['age'])

# Which type of data a dictionary can store ?
# Anything
# numbers, strings, list, dictionary.

user_info = {
    'name' : 'Siddhartha',
    'age' : 19,
    'fav_movies' : ['Coco', 'Marvel'],
    'fav_tunes' : ['fairy tale', 'song']
    
}
# print(user_info['fav_movies'])

# How to add data to empty dictionary

user_info2 ={}
user_info2 ['name'] = 'mohit'
user_info2 ['age'] = '20'
print(user_info2)