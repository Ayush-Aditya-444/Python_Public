for _ in range(int(input())):
    days, rate = map(int, input().split())
    rain = list(map(int, input().split()))
    i, cost, new = 0, 0, len(rain)
    while new != 0:
        try:
            if rain[i] == 1:
                cost += 2 * rate
                i += 2
            else:
                pass
            new -= 1
        except IndexError:
            break
    print(cost)
