import random


def get_frames(signal, size, overlap):
    start = 0
    step = int(size*overlap)
    while len(signal)-step >= start:
        lis = signal[start: start+size]
        start += step
        yield lis

signal = ([random.randint(0, 20) for i in range(20)])
for frame in get_frames(signal, size=4, overlap=0.5):
        print(frame)
