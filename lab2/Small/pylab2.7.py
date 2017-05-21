import subprocess as sp
import pyffmpeg

FFMPEG_BIN = "D:\\загрузки\\ffmpeg-3.3.1\\ffmpeg.exe"
command = [FFMPEG_BIN, '-i','','','','','','','','','','']
ffmpeg -ss 30 -t 5 -acodec copy -i in.mp3 out.mp3
# Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома
# (попурри из коротких фрагментов mp3-файлов в пользовательской директории).
# Для манипуляций со звуковыми файлами можно использовать сторонние утилиты,
# например, FFmpeg.
