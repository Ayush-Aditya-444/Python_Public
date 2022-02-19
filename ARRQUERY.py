n, Q = map(int, input().split())
N = list(map(int, input().split()))
for i in range(Q):
    p = list(map(int, input().split()))
    count = 0
    c, d = p[0] - 1, p[1]
    for j in range(c, d):
        if N[j] >= p[2]:
            count += 1
    print(count)
