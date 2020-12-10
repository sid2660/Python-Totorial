# Looping in tuples
# tuples with one element
# tuples without parenthesis
# tuples unpacking
# list inside tuples
# some functions that you can use with tuples

mixed = (1,2,3,4,0)

# for loop and tuple
# for i in mixed:
#     print(i)
#Note - You can use while loop too

# tuples with one element

nums = (1,) #Use comma to make tuples
words = ('Word1')
# print(type(nums))
# print(type(words))
# print(type(mixed))

# Tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

#Tuple unpacking
guitarists = ('Maneli jamal', 'Eddie van der meer', 'andrew foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
# print(guitarist1)
# List inside tuples
favorites = ('southern mangolia', ['Tokya ghoul theme', 'landscape'])
favorites[1].pop()
favorites[1].append('India')
# print(favorites)

## Min , Max and Sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))
