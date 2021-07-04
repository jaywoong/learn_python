import random

print('start......')



while True:
    num = random.randint(1,10)
    cnt = 0
    while True:
        cmd = input('Input Number(q:exit) .. ')
        if cmd == 'q':
            print('bye')
            break
        else:
            if cnt == 5:
                print('Fail!')
                break
            int_num = int(cmd)
            if int_num == num:
                print('Success!!!')
                break
            else:
                if int_num > num:
                    print('Lower')
                else:
                    print('Higher')
                cnt += 1
                print('Chance = ', 5 - cnt)

print('end......')
