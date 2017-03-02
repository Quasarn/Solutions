password = input('Enter password\n')
while len(password) < 10:
    password = input('Password to short\n')
options = {'digit': False, 'alpha': False, 'title': False}
quality = 0
for i in password:
    if i.isdigit():
        options['digit'] = True
        continue
    if i.istitle():
        options['title'] = True
        continue
    if i.isalpha():
        options['alpha'] = True
        continue
for k, v in options.items():
    if v:
        quality += 1
if quality == 3:
    print('Good password')
elif quality == 2:
    print('Normal password')
elif quality == 1:
    print('Bad password')
