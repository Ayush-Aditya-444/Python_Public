T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    Min = Sum = S[0]
    for i in range(1, N):
        Min = min(Min, S[i])
        Sum += Min
    print(Sum)