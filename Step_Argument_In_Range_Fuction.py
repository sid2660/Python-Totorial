# Step Argument 
# for i in range(1,11): #step is (1 ,11 , this is the place of step )
#     print(i)
# for i in range(1,11,2):
#     print(i)
    #out put is
    #1
    #3
    #5
    #7
    #9
# for i in range(10,0,-1):
#     print(i)




#Take input from user
start = int(input("Enter your start number : "))
end = int(input("Enter your end number : "))
step = int(input("Enter your step number : "))
#total = start,end,step
for i in range(start,end,step):
    print(i)