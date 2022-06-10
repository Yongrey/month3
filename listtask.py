list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]


arrays = [list1, list2, list3]
for i in arrays:
    new = i.copy()
    for n in new:
        i.append(n)
print(arrays)