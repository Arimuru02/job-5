list = [50, 65, 80, 95, 110, 1025,]
for i in list:
    print(bool([i for i in t.split() if i == '0']))
    large = (list.index(i))
    print(large)