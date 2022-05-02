def isPrime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


m, n = map(int, input().split())
if isPrime(m):
    if isPrime(n):
        c = 0
        for i in range(m, n + 1):
            if isPrime(i):
                c += 1
        if c == 2:
            print('YES')
        else:
            print('NO')

    else:
        print('NO')
