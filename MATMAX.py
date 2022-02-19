for _ in range(int(input())):
    m, n = map(int, input().split())
    p = []
    for i in range(m):
        p.append(list(map(int, input().split())))
    maxi = 0
    for i in range(m):
        if (max(p[i]) - min(p[i])) > maxi:
            maxi = max(p[i]) - min(p[i])
    print(maxi)
