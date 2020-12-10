## List Comprehension in nested list

example = [[1,2,3],[1,2,3],[1,2,3]]

nested_com = [[i for i in range(1,4)] for j in range(3)]
print(nested_com)

## 
new_list = []
for j in range(3):
    new_list.append([1,2,3])
print(new_list)
