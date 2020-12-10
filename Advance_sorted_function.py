fruits1 = ["grapes","mango","apple"]
#sort
fruits1.sort()
print(fruits1)

fruits2 = ("grapes","mango","apple")
## we can`t use sort method
##use sorted function
print(sorted(fruits2))


fruits3 = {"grapes","mango","apple"}
print(sorted(fruits3))

###

guitars = [
    {"model" : "yamaha f310", "price" : 8400},
    {"model" : "faith naptune", "price" : 50000},
    {"model" : "faith apollo venus", "price" : 35000},
    {"model" : "taylor 814ce", "price" : 450000}
]

sorted_guitar = sorted(guitars, key = lambda item : item["price"])
print(sorted_guitar)


## reverse price
sorted_guitar = sorted(guitars,key = lambda item : item["price"],reverse = True)
print(sorted_guitar)