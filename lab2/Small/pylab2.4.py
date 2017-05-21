import re


try:
    with open("C:\\Users\\Дима\\Documents\\Visual Studio 2010\\Projects\\Python\\lab2\\text2.txt", 'rt') as f:
        string = f.read()
        strings = string.split(', ')
        print(strings)
        for string in strings:
            result = re.findall(r'[\bint\b|\bbyte\b|\bshort\b]..+.=+.\d+', string)
            print(result)

except IOError as err:
    print(err)
    # Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла,
    # найти в нем с помощью регулярных выражений все подстроки определенного вида,
    # в соответствии с вариантом.
