for _ in range(int(input())):
    empty = []
    for j in range(int(input())):
        new = list(map(int, input().split()))
        empty.append(new)
    k = len(empty) - 2
    while k >= 0:
        j = 0
        while j <= k:
            empty[k][j] += max(empty[k + 1][j], empty[k + 1][j + 1])
            j += 1
        k -= 1
    print(empty[0][0])

