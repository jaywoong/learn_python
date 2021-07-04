text = '''DeFi is an open and global financial system built for the internet age – an alternative to a system that's opaque, tightly controlled, and held together by decades-old infrastructure and processes. It gives you control and visibility over your money. It gives you exposure to global markets and alternatives to your local currency or banking options. DeFi products open up financial services to anyone with an internet connection and they're largely owned and maintained by their users. So far tens of billions of dollars worth of crypto has flowed through DeFi applications and it's growing every day.'''

dic = dict()

for c in text:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1

print(dic)

ks = list(dic.keys())
ks.sort()
for k in ks:
    print('%s, %d' % (k,dic[k]))

result = sorted(dic.items(),key = lambda x : x[1], reverse=True)
print(result)

# dic2 = sorted(dic.values(), reverse = True)
# print(dic2)
#
# key_data = list(dic.keys())
# print(key_data)
# key_data.sort()
# print(key_data)
#
# for c in key_data:
#     print('%s, %d' % (c,dic[c]))