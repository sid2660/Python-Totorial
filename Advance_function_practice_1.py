## This is Challange 

## define a function take any no. of list containing number
## [1,2,3],[4,5,6],[7,8,9]
## return average
## (1+4+7)/3,(2+5+9)/3

## try to make this anonymos function in one line using lambda

l1,l2,l3 = [1,2,3],[4,5,6],[7,8,9]
def average_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder(l1,l2,l3))
    
### 
av_finder = lambda *args : [sum(i)/len(i) for i in zip(*args)]
print(av_finder(l1,l2,l3))