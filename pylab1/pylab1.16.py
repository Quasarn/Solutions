import random
import itertools
import time
import datetime
teems = ['liverpul', 'chelsi', 'arsenal', 'dinamo', 'gazmjas',
         'dojarochka', 'spartak', 'zenit', 'bavaria', 'shahter',
         'monako', 'palermo', 'csk', 'lokomotiv', 'valensia', 'ajaks']
random.shuffle(teems)
groop1 = teems[:4]
groop2 = teems[4:8]
groop3 = teems[8:12]
groop4 = teems[12:]
games = list(itertools.combinations(groop1, 2)) \
        + list(itertools.combinations(groop2, 2))\
        + list(itertools.combinations(groop3, 2)) \
        + list(itertools.combinations(groop4, 2))
dayx = datetime.date(2017, 9, 20)
delta = datetime.timedelta(days=14)
groop = True
x = 1
for i in range(len(games)):
    if groop:
        print('\nGroop', x, ':\n')
        x += 1
        groop = False
    elif (i+1) % 6 == 0:
        groop = True
    print(*games[i], ': ', dayx, ' ', '22:45')
    dayx += delta
