li = [10,20,30,40,50]

duplicate = []

for i in li:
    duplicate = duplicate + [i]

print("original list:",li)
print("duplicate list",duplicate)

if li is not duplicate:
    print("both lists are different objects")
