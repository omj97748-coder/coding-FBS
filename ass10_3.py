li = [ 10,50,30,40,20]

largest = li[0]
second = li[0]

for i in li:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
          second = i

print("second largest =",second)