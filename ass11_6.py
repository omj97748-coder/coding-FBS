list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

union = list(set(list1) | set(list2))

print("first list:",list1)
print("secnd list:",list2)
print("union:",sorted(union))