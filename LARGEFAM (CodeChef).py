for _ in range(int(input())):
# for _ in range(1):
    num = int(input())
    array = list(map(int, input().split()))
    # num = 8
    # array = [6, 2, 1, 1, 1, 1, 1, 0]
    array.sort()
    # array = [0, 1, 1, 1, 1, 1, 2, 6]
    count = 0
    i = 0
    ans = 0
    while True:
        try:
            ans += array[i]
            if ans > num - 1:
                ans -= array[i]
                count -= 1
                pass
            count += 1
            i += 1
        except IndexError:
            break
    print(count)