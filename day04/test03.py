def calc(n1 ,op ,n2):
    result = 0
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    else:
        result = 0
    return result

num1 = input('Input num1...')
num2 = input('Input num2...')
op = input('Input op...')

data = calc(int(num1), op , int(num2))
print(data)