import csv
import sys

# datas = ['1', '2', '']
#
# sum = 0
# for d in datas:
#     if d == None or d == '':
#         continue
#     num = int(d)
#     sum += num
# print(sum)

f = open('c:\\mydata\\ta_2021.csv')
data = csv.reader(f)
header = next(data)
print(header)
print('---------------------')

# high = []
# low = []
#
# for row in data:
#     h = float(row[4])
#     l = float(row[3])
#     high.append(h)
#     low.append(l)
#
# print(max(high))
# print(min(low))

max = 0.0
max_date = ''
min = 999
min_date = ''
for row in data:
    if max < float(row[-1]):
        max = float(row[-1])
        max_date = row[0]
    if min < float(row[-2]):
        min = float(row[-2])
        min_date = row[0]
print('%s, %.2f' % (max_date, max))
print('%s, %.2f' % (min_date, min))