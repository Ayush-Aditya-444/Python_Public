year = int(input())
n = True
c = 0
while n:
    year += 1
    y = str(year)
    for i in range(len(y)):
        if y.count(y[i]) == 1:
            c = 1
            continue
        else:
            c = 0
            break
    if c == 1:
        print(year)
        n = False
    else:
        continue
