t = int(input())
for i in range(t):
       d, n =map(int, input().split())
       for j in range(d):
              sum = n*(n+1)/2
              n = sum
       print(int(n))