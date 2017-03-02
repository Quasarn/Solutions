try:
    number = float(input("Enter number\n"))
    if number > 0:
        rub = int(number)
        kop = int((number-rub)*100)
        print(rub, 'rub ', kop, 'kop')
    else:
        raise ValueError
except ValueError:
    print('Error')
