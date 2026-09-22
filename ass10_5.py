li = [ 10,20,10,30,10,40,20]

num = int(input("enter number:"))

count = 0

for i in li:
    if i == num:
        count = count + 1

if count > 0:
    print("element is present")
    print("occurrences =", count)
else:
    print("element is not present")