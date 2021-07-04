def calc(op ,*n):
    result = 0
    if op == '+':
        result = n[0] + n[1]
    elif op == '-':
        result = n[0] - n[1]
    elif op == '*':
        result = n[0] * n[1]
    elif op == '/':
        result = n[0] / n[1]
    else:
        result = 0
    return result

num1 = input('Input num1...')
num2 = input('Input num2...')
op = input('Input op...')

data = calc(op , int(num2) , int(num2))
print(data)