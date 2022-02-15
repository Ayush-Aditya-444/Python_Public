for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if b == a:
        ans = 0
    else:
        for j in range(c):
            if a < b:
                a += 1
            elif a > b:
                b += 1
    ans = abs(a - b)
    print(abs(ans))
