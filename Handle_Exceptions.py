## Exception Handling
## Try except else finally
# while True:
#     try: 
#         age = int(input("Enter your age : "))
#         break
#     except:
#         print("Invalid Input.... Please try again ")
        
        
# if age < 18:
#     print("You can`t play this game")
# else:
#     print("You can play this game")


#### else and finally clause in exception handling
while True:
    try: 
        age = int(input("Enter your age : "))
    except ValueError:
        print("Please type number !!!!")
    except:
        print("Invalid Input.... Please try again!!!! ")
    else:
        print(f"user input = {age}")
        break
    finally:
        print("Finally blocks ......")
        