#login system with 3 attempts

username = "Samn"
password = "Samn123"

for i in range(3):
    user = input("Enter username: ")
    pswd = input("Enter password: ")
    
    if user == username and pswd == password:
        print("Login successful!!")
        break
    else:
        print("Wrong username or password!")
        
        # If this was the last attempt:
        if i == 2:
            print("3 attempts finished!!")