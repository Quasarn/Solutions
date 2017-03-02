text = input('Enter Text\n')
hist = {}
for i in text:
    hist[i] = hist.get(i, 0) + 1
for k, v in hist.items():
    if v == 1:
        print(k)
