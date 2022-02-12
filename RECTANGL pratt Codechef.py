for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == b and c == d:
        print('YES')
    elif a == c and b == d:
        print('YES')
    elif b == c and a == d:
        print('YES')
    else:
        print('NO')