data = [1,2,3,4,5]

su = 0
for d in data:
    su += d
print(su)

su2 = 0
for i in range(0,len(data)):
    su2 += data[i]
print(su2)

print(sum(data))

