for _ in range(int(input())):
    num = sum(list(map(int, input().split())))
    for t in range(num + 1, num + 50):
        count = 0
        for i in range(1, t + 1):
            if t % i == 0:
                count += 1
        if count == 2:
            new = t
            break
    print(t - num)
