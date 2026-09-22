li = [10,20,30,20,40,20,50]

num =int(input("enter element remove:"))

new_list =[]

for i in li:
    if i != num:
        new_list = new_list + [i]

print("original list:",li)
print("list after removing",num,":" ,new_list)