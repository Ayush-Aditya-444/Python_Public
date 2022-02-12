for _ in range(int(input())):
    num, count = int(input()), 0
    for i in range(30):
        if num % 10 != 0:
            num = 2 * num
            count += 1
        else:
            break
    if num % 10 != 0:
        count = -1
    print(count)
