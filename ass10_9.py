li = [ 10,15,20,25,30,35,40]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even = even + [i]
    else:
        odd = odd + [i]

print("original list:",li)
print("even element:",even)
print("odd element:",odd)