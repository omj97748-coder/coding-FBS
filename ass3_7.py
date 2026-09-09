# write a program to check if user has entered correct userid and password.

userid = input("Enter user id = ")
password = (input("Enter password = "))

if userid == "admin" and password == "2005":
    print("Login Successful")
else:
    print("Invalid User ID or Password")