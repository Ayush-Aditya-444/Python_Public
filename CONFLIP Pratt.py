for _ in range(int(input())):
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if b % 2 == 0:
            print(int(b / 2))
        elif a == 1 and b % 2 != 0:
            if c == 1:
                print(int(b / 2))
            elif c == 2:
                print((b // 2) + 1)
        elif a == 2 and b % 2 == 0:
            print(print(int(b / 2)))
        elif a == 2 and b % 2 != 0:
            if c == 1:
                print((b // 2) + 1)
            elif c == 2:
                print(int(b / 2))
