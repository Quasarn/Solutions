number = input('Enter number\n')
if number.isdigit():
    if len(number) < 16:
        print('Enter more numbers\n')
    number = number[:16]
    print(number[:4], '*'*8, number[-4:])
else:
    print('Error')
