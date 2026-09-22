list = [25,10,45,5,30]

maximum = list[0]
minumum = list[0]

for i in list:
    if i > maximum:
        maximum = i
    if i < minumum :
        minumum = i

print("list:", i)
print("maximum =", maximum)
print("minumum =", minumum)