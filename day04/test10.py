def insert():
    print(id, pwd, name)
    print('Inserted Data .....')
def selectone(id):
    print('Selected One Data .....')
    return [id,'pwdxx','jamesxx']
def select():
    print('Selected Data .....')
    datas = [['id01','pwd01','james1'],
             ['id02','pwd02','james2'],
             ['id03','pwd03','james3'],
             ['id04','pwd04','james4']]
    return datas
def update():
    print(id, pwd, name)
    print('updated Data .....')
def delete():
    print(id)
    print('Deleted Data .....')

while True:
    cmd = input('Input Command(i,s,so,u,d,q)...')
    if cmd == 'q':
        print('bye')
        break
    elif cmd == 'i':
        id = input('Input ID')
        pwd = input('Input Password')
        name = input('Input Name')
        insert(id, pwd, name)
    elif cmd == 'u':
        id = input('Input ID')
        pwd = input('Input Password')
        name = input('Input Name')
        update(id, pwd, name)
    elif cmd == 'd':
        id = input('Input ID')
        delete(id)
    elif cmd == 's':
        users = select()
        for u in users:
            print(u)
    elif cmd == 'so':
        id = input('Input ID')
        user = selectone(id)
        print(user)



print('End Program ...')