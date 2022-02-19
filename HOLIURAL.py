for _ in range(int(input())):
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    maxi = float("inf")
    for i in range(len(p)):
        if ((p[i] * b) + q[i]) < maxi:
            maxi = ((p[i] * b) + q[i])
    print(maxi)
