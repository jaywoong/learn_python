def score(name, *s, **option):
    print(name)
    sum = 0
    for i in s:
        sum += i
    print(sum)
    if option['avg'] == True:
        print(sum/len(s))

help(min)

score('LEE', 88, 99, 100, 68, avg = True )
print('--------------------------------')
score('KIM', 88, 99, 100, avg = False )
