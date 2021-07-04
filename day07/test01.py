import random

dic = dict()    # {}
datas = {1, 2, 3, 4, 5} #집합

print(type(datas))
datas.add(6) #집합은 add 메소드 사용
print(datas)
datas.remove(2)
print(datas)
datas.add(5)
print(datas)    #중복불가

list_data = [1, 2, 3, 4, 5, 5, 5]
set_data = set(list_data)
print(set_data)

# 1 - 45 중 랜덤 숫자 6개
nums = set()
while True:
    a = random.randint(1, 45)
    nums.add(a)
    if len(nums) == 6:
        break
print(nums)

s1 = [1, 2, 3, 4]
s2 = [3, 4, 5, 6]
ss1 = set(s1)
ss2 = set(s2)
ss1.update(ss2)
print(ss1)
result = list(ss1)
print(result)
