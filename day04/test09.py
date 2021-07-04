# 변수(variable) 영역
import random

data = 0
num = 0

# 함수(function) 영역
def func():
    global num
    num = 200
    data = 100
    return data

# 코드 영역
result = func()
print(result)
print(data)
print(num)

max_data = max(8,9,10,100,9000000)
print(max_data)

min_data = min(8,9,10,100,9000000)
print(min_data)

rnum = random.randint(1, 10)
rr = round(10.123238, 5)
print(rr)

stri = '10 + 20 + 30'
print(eval(stri)) # string 형태를 계산해줌

int('100')
str(100)
print(float('100')) # 실수

print(hex(70))  # 16진수
print(oct(10))  # 8진수
print(bin(10))  # 2진수

print(sum([1,2,3,4,5,6,7,8,9,10]))  # sum에는 리스트
