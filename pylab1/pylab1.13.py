def extra_enumerate(sequence, start=0):
    total_sum = sum(sequence)
    cum = 0
    for elem in sequence:
        cum += elem
        frac = cum / total_sum
        yield elem, cum, frac

sequence = [1, 3, 4, 2]
for elem, cum, frac in extra_enumerate(sequence):
    print("({}, {}, {})".format(elem, cum, frac), end="; ")
