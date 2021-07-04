st = ['id', 'pwd', 'name', 'age']
data = ['id01', 'pwd01', 'james', 30]

cust = zip(st,data)
print(cust)

for s,d in cust:
    print('%s : %s' % (s,d))

dic_cust = dict(zip(st,data))
print(dic_cust)