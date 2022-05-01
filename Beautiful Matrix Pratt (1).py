a = []
for _1 in range(5):
    a.append(list(map(int, input().split())))
b, c = 0, 0
for _3 in range(5):
    for _4 in range(5):
        if a[_3][_4] == 1:
            b, c = _3, _4
print(abs(2 - b) + abs(2 - c))
