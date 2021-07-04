tu1 = 1,2,3,4,5

print(tu1)
print(type(tu1))

print(tu1[1:])

print(sum(tu1)/len(tu1))

list_data = list(tu1)
list_data[2] = 100

tu1 = tuple(list_data)
print(tu1)