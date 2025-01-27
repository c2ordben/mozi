import random
ar=[2500, 2100, 1300, 0]
jegy = 6
def nezoter():
    for i in range(15):
        kislista=[]
        for j in range(10):
            kislista.append(random.choice(ar))
        kislista.append('|')
        for j in range(10):
            kislista.append(random.choice(ar))
        print(kislista)
nezoter()
def jegyek():
    print('Mennyi jegyet szeretne?')
    a = int(input())
    while a < 2 and a > 5 and 1 < a > 6:
        if a > 5:
            print('maximum 5 jegyet lehet vásárolni')
        elif a < 2:
            print('minimum 2 jegyet kell venni')
        else:
jegyek()