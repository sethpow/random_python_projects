# MAP
x = [4423, 4, 234, 2, 4234, 23432, 42, 34, 35, 43654, 64, 574]

mp = map(lambda i: i * 2, x)
print(*mp)


# FILTER
fl = filter(lambda i: i % 2 == 0, x)
print(*fl)