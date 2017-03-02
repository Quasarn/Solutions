text = ['www.jhdfg.com', 'jdfghkd.com', 'www.fghfg']
text2 = ['http.' + i if i.endswith('.com') else 'http.' + i + '.com' for i in text if i.startswith('www.')]
print(text2)
