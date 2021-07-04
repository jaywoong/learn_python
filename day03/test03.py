for i in range(1,13):
    if i % 2 == 1:
        print(i)
print('_________________________')

s = 1

while s < 13:
    if s % 2 == 0:
        print(s)
    s+=1

print('_________________________')

cnt = 0
sum = 0

for j in range(1, 101):
    if j % 2 == 1 and j % 3 == 0:
        sum += j
        cnt += 1
print(cnt)
print(sum)
print(sum/cnt)

print('_________________________')

k = 1
sum2 = 0
cnt2 = 0

while k < 101:
    if k % 2 == 1 and k % 3 == 0:
        sum2 += k
        cnt2 += 1
    k += 1

print(cnt2)
print(sum2)
print(sum2/cnt2)
