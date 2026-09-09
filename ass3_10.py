# write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
# input gender and age
gender = input("enter gender (male/female):")
age = int(input("enter age:"))

# check eligibility 
if (gender == "male" and age >=21) or (gender == "female" and age >=18):
    print("eligible for marriage")
else:
    print("not eligible for marriage")
    