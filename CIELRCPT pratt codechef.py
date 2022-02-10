amount = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
for _ in range(int(input())):
    num = int(input())
    i, count = -1, 0
    while num != 0:
        if amount[i] < num:
            num -= amount[i]
            count += 1
        elif amount[i] == num:
            num -= amount[i]
            count += 1
            break
        else:
            i -= 1
    print(count)
