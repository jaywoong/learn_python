print('start......')

while True:
    cmd = input('Input Command..')
    if cmd == 'q':
        print('bye')
        break
    elif cmd == 'i':
        print('Insert Data ...')
    elif cmd == 'd':
        print('Delete Data ...')
    elif cmd == 'u':
        print('Update Data ...')
    elif cmd == 's':
        y = input('Input Year..')
        print(y, '  Select Data ...')
    else:
        print('Invalid Cmd.. Try again..')

print(cmd)
print('end......')
