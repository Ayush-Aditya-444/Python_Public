for _ in range(int(input())):
    n, k = map(int, input().split())
    m = 0
    for j in range(1, k + 1):
        m = max(m, n % j)
    print(m)
