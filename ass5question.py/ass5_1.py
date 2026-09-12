# 1. write a program to prompt user to enter userid and password . if id and
# password is incorrect give him chance to enter the credentials.let him try 3 times.
# after that programs  to terminates.

userid = "admin"
password = "admin123"

for i in range(1,4):
    uid = input("enter userid:")
    pwd = input("enter password:")

    if uid == userid and pwd == password:
        print("login successful")
        break
    else:
        print("incrorrect user id or password ")

        if i == 3:
            print("program terminated")