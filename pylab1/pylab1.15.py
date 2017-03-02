import random


def pre_process(a):
    def fff(funk):
        tmp2 = s[0]
        for i in range(len(s)):
            tmp = s[i]
            s[i] = round(s[i] - a * tmp2, 1)
            tmp2 = tmp
        return funk(s)
    return fff


s = ([random.randint(0, 10) for i in range(5)])
print(s)


@pre_process(a=0.5)
def plot_signal(s):
    for sample in s:
        print(sample, end=' ')
