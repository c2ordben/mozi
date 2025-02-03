import random

ar=[2500, 2100, 1300, 0]
nezoterek=[]
print('hány jegyet szeretne? (2-5)')
a = int(input())

while a > 5 or a < 2:
    print('2-5db jegyet válasszon!')
    a = int(input())


def nezoter():
    for i in range(15):
        sorok=[]
        for i in range(10):
            sorok.append(random.choice(ar))
        sorok.append('____')
        for i in range(10):
            sorok.append(random.choice(ar))
        print(sorok)
        nezoterek.append(sorok)


def bevetel(nezoterek):
    osszeg = 0
    for i in range(len(nezoterek)):
        for j in range(len(nezoterek[i])):
            if nezoterek[i][j] == 0:
                osszeg += 0
            if nezoterek[i][j] == 1300:
                osszeg += 1300
            if nezoterek[i][j] == 2100:
                osszeg += 2100
            if nezoterek[i][j] == 2500:
                osszeg += 3500
    print(osszeg, 'az összes bevétel')


def TeremKihasznaltsag(nezoterek):
    szabadHely = 300
    for i in range(len(nezoterek)):
        for j in range(len(nezoterek[i])):
            if nezoterek[i][j] == 0:
                szabadHely -= 1
    print(round((szabadHely / 300)*100, 2),'%','hely foglalt')


def FelnottJegyek(nezoterek):
    felnott = 0
    for i in range(len(nezoterek)):
        for j in range(len(nezoterek[i])):
            if nezoterek[i][j] == 2500:
                felnott += 1
    print(felnott,'db teljes jegyet vettek')


def JegySzam(a):
    if a == 2:
        sor = 0
        for i in range(len(nezoterek)):
            for j in range(len(nezoterek[i])):
                    if nezoterek[i][j] == 0 and nezoterek[i][j-1] == 0:
                        sor = i+1
                        print(sor, '. sorban van 2 hely')
                        return
    if a == 3:
        sor = 0
        for i in range(len(nezoterek)):
            for j in range(len(nezoterek[i])):
                    if nezoterek[i][j] == 0 and nezoterek[i][j-1] == 0 and nezoterek[i][j-2] == 0:
                        sor = i+1
                        print(sor, '. sorban van 3 hely')
                        return
    if a == 4:
        sor = 0
        for i in range(len(nezoterek)):
            for j in range(len(nezoterek[i])):
                    if nezoterek[i][j] == 0 and nezoterek[i][j-1] == 0 and nezoterek[i][j-2] == 0 and nezoterek[i][j-3] == 0:
                        sor = i+1
                        print(sor, '. sorban van 4 hely')
                        return
    if a == 5:
        sor = 0
        for i in range(len(nezoterek)):
            for j in range(len(nezoterek[i])):
                    if nezoterek[i][j] == 0 and nezoterek[i][j-1] == 0 and nezoterek[i][j-2] == 0 and nezoterek[i][j-3] == 0 and nezoterek[i][j-4] == 0:
                        sor = i+1
                        print(sor, '. sorban van 5 hely')
                        return
    print('nincs')



nezoter()
JegySzam(a)
bevetel(nezoterek)
TeremKihasznaltsag(nezoterek)
FelnottJegyek(nezoterek)

