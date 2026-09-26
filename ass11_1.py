numbers = [10,15,20,25,30,35,40]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("original list:",numbers)
print("even list:",even)
print("odd list:",odd)    