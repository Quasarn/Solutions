money = {5000: 1, 1000: 2, 500: 3, 100: 4, 50: 5, 10: 6}
cash = int(input('how much money?\n'))
summ = 0
cashinhand = {}
for k, v in money.items():
    summ += (k*v)
print(summ)
if summ < cash:
    print('Error')
else:
    tmp = 0
    for k, v in money.items():
        tmp = cash // k
        if 0 < tmp <= v:
            cashinhand[k] = tmp
            cash -= k*tmp
        elif tmp > 0:
            cashinhand[k] = v
            cash -= k * v
    for k, v in cashinhand.items():
        print("{}*{}".format(k, v), end='+')
