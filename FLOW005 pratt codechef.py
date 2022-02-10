denominations = [1, 2, 5, 10, 50, 100]
for _ in range(int(input())):
    note = int(input())
    i, counties = -1, 0
    while note != 0:
        if denominations[i] < note:
            note -= denominations[i]
            counties += 1
        elif denominations[i] == note:
            note -= denominations[i]
            counties += 1
            break
        else:
            i -= 1
    print(counties)
