## In keywor and iterations in dictionary

user_info = {
    'name' : 'Siddhartha',
    'age' : 19,
    'fav_movies' : ['Coco', 'Marvel'],
    'fav_tunes' : ['fairy tale', 'song']
    
}

## Cheak if key exist in dictionary
# if 'name' in user_info:
#     print('Present')
# else:
#     print('Not Present')

## Cheak if values exiest in dictionary (.values use to find values in dictionary)
# if 19 in user_info.values():
#     print('Present')
# else:
#     print('Not Present') 

## Loops in dictionaries

# for i in user_info:
    # print(i)
    
# for i in user_info.values():
#     print(i)

## Values Method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

##  Keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

## Loops in dictionaries

# for i in user_info:
#     print(user_info[i])

## Items method 
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

#####
for key, value in user_info.items():
    print(f"key is {key} and value is {value}")
    