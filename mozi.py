#15 sor
#20 szék
#felnőtt: 2500
#diák/nyugdíjas: 2100
#gyerek: 1300

import random

ar=[2500, 2100, 1300]
jegyek = 6

def nezoter():
    for i in range(15):
        kislista=[]
        for j in range(10):
            kislista.append(random.choice(ar))
        kislista.append('|')
        for j in range(10):
            kislista.append(random.choice(ar))
