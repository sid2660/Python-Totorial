def user_info(first_name , Last_name = None , age = 0): # Pass the default pyrameaters
    print(f"Your First name is {first_name}")
    print(f"Your last name is {Last_name}")
    print(f"Your age is {age}")
first_name,Last_name = input("Enter your First and last name : ").split(" ")
age = int(input("Enter your age : "))
user_info(first_name, Last_name, age)