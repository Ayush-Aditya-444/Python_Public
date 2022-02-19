def isPrime(n):
    for j in range(2, n):
        if n % j == 0:
            return False


for _ in range(int(input())):
    num = int(input())
    c, count = num, 0
    num = int(num / 2)
    for i in range(1, num + 1):
        if isPrime(i) is None and isPrime(c - i) is None:
            print(i, c - i)
            count += 1
            break
    if count == 0:
        print(-1, -1)
