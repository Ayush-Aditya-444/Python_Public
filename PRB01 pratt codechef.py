for _ in range(int(input())):
    num, count = int(input()), 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print('yes')
    else:
        print('no')
