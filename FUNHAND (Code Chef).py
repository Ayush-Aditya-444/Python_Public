# cook your dish here
for _ in range(int(input())):
    N, a, b = map(int, input().split())
    t = [i for i in range(1, N + 1)]
    if N < 3:
        print(0)
    else:
        if abs(a - b) == 1:
            if a + 1 in t and b - 1 in t and a > b:
                print(2)
                continue
            if a - 1 in t and b + 1 in t and b > a:
                print(2)
                continue
            if a - 1 in t or b + 1 in t:
                print(1)
                continue
        elif abs(a - b) == 2:
            print(1)
        else:
            print(0)