## Word Conter 
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count
# print(word_counter('siddhartha'))



### Exercise

## User = {
#     'name' =  'Siddhartha',
#     'age' = 19,
#     'fav_movies' = ['M1', 'M2']
#     'fav_songs' = ['s1', 's2']
    
# }

user = { }

name = input('Enter your name : ')
age = input('Enter your age : ')
fav_movies = input('Fav movies seprated by comma : ').split(',')
fav_song = input('Fav songs seprated by comma : ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song

for key, value in user.item():
    print(f"{key} : {value}")