import calc
try:
    data = calc.calc(10)
    result = data * 1000
    print(result)
except ZeroDivisionError:
    print('Zero Division Error')
except ValueError:
    print('Value Error')
