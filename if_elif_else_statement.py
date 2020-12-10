#Show ticket pricing
#0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# 60 above (200)
age = int(input("Enter your age : "))
if age==0 or age<0:#this for whome who enter 0 oe -(ve)
    print("you cannot watch")
elif 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200  ")