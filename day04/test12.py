st1 = 'jmlee@tonesol.co.kr'

print(len(st1))
print(st1.find('.'))
print(st1.rfind('.'))
print(st1.count('.'))


id = st1[:st1.find('@')]
print(id)
domain = st1[st1.find('@')+1:st1.find('.')]
print(domain)