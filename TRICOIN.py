for _ in range(int(input())):
    num = int(input())
    i, j, count = 0, 0, 0
    while True:
        i += 1
        j += i
        if j > num:
            break
        else:
            count += 1
    print(count)
