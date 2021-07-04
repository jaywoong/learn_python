from value import Account

acc = None

while True:
    b1=0
    b2=0
    b3=0
    i=0
    cmd = input('input cmd(c, s, d, w, q)')
    if cmd == 'q':
        break
    elif cmd == 'c':
        print('Create')
        b1 = int(input('money'))
        i = float(input('interest'))
        acc = Account(b1,i)
        print(acc)

    elif cmd == 's':
        print('Select')
        if acc != None:
            print(acc)
        else:
            print('Not exist')

    elif cmd == 'd':
        b2 = int(input('money'))
        acc.deposit(b2)

    elif cmd == 'w':
        b3 = int(input('money'))
        try:
            acc.withdraw(b3)
        except ValueError as v:
            print(v.args[0])
