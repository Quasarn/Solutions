try:
    f = open('C:\\Users\\Дима\\Documents\\Visual Studio 2010\\Projects\\Python\\lab2\\text.txt')
    text = f.read()
    text = text.lower()
    hist = {}
    for i in text:
        if i.isalpha():
            hist[i] = hist.get(i, 0) + 1
    print(sorted(hist.items(), key=lambda x: x[1], reverse=True))
except IOError as err:
    print('ERROR')
except:
    print('Uncnown ERROR')
finally:
    if f:
        f.close()
# Напишите скрипт, который читает текстовый файл и выводит символы в порядке
# убывания частоты встречаемости в тексте. Регистр символа не имеет значения.
# Программа должна учитывать только буквенные символы (символы пунктуации, цифры
# и служебные символы слудет игнорировать). Проверьте работу скрипта на нескольких
# файлах с текстом на английском и русском языках, сравните результаты с таблицами,
# приведенными в wikipedia.org/wiki/Letter_frequencies.
