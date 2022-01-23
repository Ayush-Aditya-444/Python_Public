T = int(input())
for i in range(0, T):
    n, k = map(int, input().split())
    ans = 1
    for j in range(1, k):
        ans *= n - k + j
        ans //= j
    print(int(ans))