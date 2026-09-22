li = [ 1,2,3,4,5]

square = []
cube = []

for i in li:
    square = square + [i * i]
    cube = cube + [ i * i * i]

print("numbers:",li)
print("square:",square)
print("cube:",cube)