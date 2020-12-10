## List Inside List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
## 3 list -------> 3 items inside the list
# print(matrix[0]) ## print the zero`th position list items. 
# for i in matrix:
#     print(i)

for sublist in matrix:
    for i in sublist:
        print(i, end=(" "))
print(matrix [1][1]) ## list inside list print the firts list position and second list position. 


# #Type fuction
# s = "String"
# print(type(s)) ### It`s show the class of the string . 
# print(type(matrix))
