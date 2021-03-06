import os


musicFolder = "D:\\музыка\\Черный Обелиск"
songsFile = "D:\\музыка\\Черный Обелиск\\songs.txt"

try:
    with open(songsFile, 'rt') as f:
        formatSongs = f.read()
        formatSongs = formatSongs.split(', ')
        print(formatSongs)

except IOError as err:
    print(err)

for file in os.listdir(musicFolder):
    if os.path.isfile(musicFolder + '\\' + file):
        for song in formatSongs:
            if file in song:
                os.rename(musicFolder + '\\' + file, musicFolder + '\\' + song)

# Задан путь к директории с музыкальными файлами (в названии которых нет номеров,
# а только названия песен) и текстовый файл, хранящий полный список песен с номерами
# и названиями в виде строк формата «01. Freefall [6:12]». Напишите скрипт, который
# корректирует имена файлов в директории на основе текста списка песен.
