text = input('Enter text\n')
text.replace(',', '')
words = text.split(' ')
for i in range(len(words)):
    if len(words[i]) > 7:
        print((words[i]))
for i in range(len(words)):
    if 4 <= len(words[i]) <= 7:
        print((words[i]))
for i in range(len(words)):
    if len(words[i]) < 4:
        print((words[i]))
print(words)
