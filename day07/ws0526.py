import csv

f = open('c:\\mydata\\daily.csv')
data = csv.reader(f)
header = next(data)
print(header)

month_temp = dict()
day = 0
for d in data:
    month = d[0][d[0].find('-') + 1 : d[0].rfind('-')]
    if month not in month_temp:
        month_temp[month] = float(d[2])
        day = 1
    else:
        month_temp[month] = month_temp[month] * day
        day += 1
        month_temp[month] += float(d[2])
        month_temp[month] = month_temp[month] / day

print(month_temp.values())
