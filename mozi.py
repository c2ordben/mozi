import random
ar=[2500, 2100, 1300, 0]
nezoterek=[]
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
    print(felnott,'felnőtt jegyet vettek')


def JegyekSzama():
    if 


nezoter()
bevetel(nezoterek)
TeremKihasznaltsag(nezoterek)
FelnottJegyek(nezoterek)
