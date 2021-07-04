for i in range (1,11):
    stop = False
    for j in range(1,11):
        if i == 3 and j == 5:
            stop = True
            break
        print(i,':',j);
    if stop == True:
        break
    print(i, '------------')