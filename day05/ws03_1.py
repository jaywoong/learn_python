score = [
    ['2019-01-03',10,12,14,10],
    ['2020-02-03',12,12,14,11],
    ['2020-03-03',13,13,15,12],
    ['2020-03-03',14,14,16,13],
    ['2020-04-03',15,15,17,14],
]

temps = [0,0,0,0,0,0,0,0,0,0,0,0]
cnt   = [0,0,0,0,0,0,0,0,0,0,0,0]

for data in score:
    if '2020' in data[0]:
        for i in range(1,13):
            if int(data[0][data[0].find('-')+1 : data[0].rfind('-')]) == i:
                for tt in data[1:]:
                    temps[i-1] += tt
                    cnt[i-1] += 1

print(temps)
print(cnt)

for i in range(0,12):
    if cnt[i] !=0 and temps[i] !=0:
        print('%d월의 평균 기온은 %.2f'% (i+1, temps[i]/cnt[i]))