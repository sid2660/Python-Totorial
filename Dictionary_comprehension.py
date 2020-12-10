## Dictionary Comprehension
## square = {1:1, 2:4, 3:9}

square = {f"square of {num} is":num**2 for num in range(1,11)}
print(square)
## single line print
for k,v in square.items():
    print(f"{k} : {v}")
    
## Count char.
## "Siddhartha"
string = "Siddhartha"
word_count = {char:string.count(char) for char in string}
print(word_count)
## single line print
for i,j in word_count.items():
    print(f"{i}:{j}")