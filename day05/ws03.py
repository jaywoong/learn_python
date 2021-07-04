score = [
    ['2019-01-03',10,12,14,10],
    ['2020-02-03',12,12,14,11],
    ['2020-03-03',13,13,15,12],
    ['2020-03-03',14,14,16,13],
    ['2020-04-03',15,15,17,14],
]
sum2=0
sum3=0
sum4=0
for data in score:
    if data[0].startswith('2020-02'):
        for i in data[1:]:
            sum2 += i
    elif data[0].startswith('2020-03'):
        for i in data[1:]:
            sum3 += i
    elif data[0].startswith('2020-04'):
        for i in data[1:]:
            sum4 += i
print('2020년 02월 %.2f' % (sum2 / len(data[1:])))
print('2020년 02월 %.2f' % (sum3 / len(data[1:])))
print('2020년 02월 %.2f' % (sum4 / len(data[1:])))
