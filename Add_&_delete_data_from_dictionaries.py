## Add and Delete data 

user_info = {
    'name' : 'Siddhartha',
    'age' : 19,
    'fav_movies' : ['Coco', 'Marvel'],
    'fav_tunes' : ['fairy tale', 'song']
    
}

## How to add data 
# user_info['fav_song'] = ['song1', 'song2']
# print(user_info)

## Pop Method 
# popped_item = user_info.pop('fav_tunes')
# print(f"popped item is {popped_item}")
# print(user_info)

## Popped items
Popped_item = user_info.popitem()
print(user_info)
print(Popped_item)