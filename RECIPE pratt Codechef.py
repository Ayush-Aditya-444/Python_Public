from math import gcd
for t in range(int(input())):
    new = list(map(int, input().split()))

    N = new.pop(0)

    g = new[0]

    for i in range(1, len(new)):
        g = gcd(g, new[i])

    for i in range(N):
        new[i] //= g

    print(*new)
