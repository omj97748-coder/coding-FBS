li = [10,20,10,30,20,40,30]

new_list = []

for i in li:
    found = False

    for j in new_list:
        if i == j:
            found = True
            break

    if found == False:
        new_list.append(i)

print("original list =",li)
print("list without duplicates =",new_list)