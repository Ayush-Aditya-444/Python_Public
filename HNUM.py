for _ in range(int(input())):
    num = int(input())
    new = [int(i) for i in str(num)]
    ans = num % sum(new)
    if ans == 0:
        print('Yes')
    else:
        print('No')
