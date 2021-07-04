import random
lotto = []

def rand():
    while len(lotto) == 7:
        r = random.randint(1,46)
        if r not in lotto:
            r.append(lotto)

lotto = rand()
print(lotto)
