#Replace() Method
#Find() Method

string = "She is beautiful and she is good dancer is"
#Replace method
print(string.replace(" ",""))#replace all space to no space
print(string.replace("is","was"))# is replace by was
print(string.replace("is","was",1))#only one is replace and other  not
#Find method 
print(string.find("is"))#find the position of (is)
print(string.find("is",5))#To find the another (is) position in the string
#find the another position of (is)
is_pos1= string.find("is")# is_pos1 ____>
is_pos2= string.find("is") #is_pos2
print(is_pos2)
