import random

def check():
    cor = 0
    for i in num:
        if i in lotto:
            cor += 1
    return cor

while True:
    money = []
    num = []
    lotto = []
    n = 0
    cnt = 0

    while len(num) <= 6:
        n = int(input('Input your number'))
        if n in num:
            print('Already exists')
        elif n <= 0 or n > 45:
            print('Invalid Number')
        else:
            num.append(n)

    while len(lotto) <= 6:
        r = random.randint(1,46)
        if r not in lotto:
            lotto.append(r)

    for i in range(0,3):
        w = random.randint(1000000,10000000000)
        money.append(w)
    money.sort(reverse=True)

    result = check()

    if result == 6:
        print('1등! 상금은 %d원 입니다.' % (money[0]))
    elif result == 5:
        print('2등! 상금은 %d원 입니다.' % (money[1]))
    elif result == 4:
        print('3등! 상금은 %d원 입니다.' % (money[2]))
    else:
        print('꽝! 당첨 번호는 %s 입니다.' % (lotto))




