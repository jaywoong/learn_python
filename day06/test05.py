import random

while True:
    num = 0
    cnt = 0
    r = 0
    ran = []
    num = int(input('Input number..?'))
    if num > 0 and num < 10:
        for i in range(0,20):
            r = random.randint(0,10)
            ran.append(r)
        for k in ran:
            if k == num:
                cnt += 1
        print(cnt)






