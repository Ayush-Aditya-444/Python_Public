for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b and a < c:
        print('Draw')
    elif b < a and b < c:
        print('Bob')
    elif c < a and c < b:
        print('Alice')
