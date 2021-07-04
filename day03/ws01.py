sum3 = 0
sum7 = 0

for i in range(1,101):
    if i % 3 == 0:
        sum3 += i
    if i % 7 == 0:
        sum7 += i

print(sum3 - sum7)