# Min Max function 

number = [6, 60, 2]
# print(min(number)) #### Min is used for finding minimum numbers of the list. 
# print(max(number)) ### Max is used for finding maximum numbers of the list. 

## Find a greatest diffrence numbers b/w max and min number

def grt_dif(l):
    return max(l) - min(l) 
print(grt_dif(number))