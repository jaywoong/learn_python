data = ['2020-05-24', 20, 30, 32]
print(data[-1])
print(len(data))
print('----------------')
for i in data:
    print(i)

print('----------------')
sum = 0
for i in data[1:len(data)]:
    sum += i

print('%s의 평균온도는 %f도 입니다.' % (data[0], sum/len(data[1:])))