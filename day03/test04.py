cnt = 0
sum = 0
cnt2 = 0
sum2 = 0

for i in range(1, 101):
    if i % 2 == 1:
        sum += i
        cnt += 1
    else:
        sum2 += i
        cnt2 += 1

print(cnt)
print(sum)
print(sum/cnt)
print(cnt2)
print(sum2)
print(sum2/cnt2)
print('-----------------------')

cnt3 = 0
sum3 = 0
cnt4 = 0
sum4 = 0
cnt5 = 0
sum5 = 0

for i in range(1, 1000):
    if i % 2 == 0:
        sum3 += i
        cnt3 += 1
    if i % 3 == 0:
        sum4 += i
        cnt4 += 1
    if i % 5 == 0:
        sum5 += i
        cnt5 += 1


print(cnt3)
print(sum3)
print(sum3/cnt3,'\n')
print(cnt4)
print(sum4)
print(sum4/cnt4,'\n')
print(cnt5)
print(sum5)
print(sum5/cnt5)