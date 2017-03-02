text = input('Enter Text\n')
newtext = text.split(' ')
result = ''
for i in range(len(newtext)):
    if newtext[i][0].isupper():
        result = result + newtext[i].upper()+' '
    else:
        result = result + newtext[i]+' '
print(result)
