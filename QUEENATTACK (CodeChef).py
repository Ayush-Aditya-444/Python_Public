# cook your dish here
for _ in range(int(input())):
     n,x,y = list(map(int,input().split()))
     r = 2*n-2
     r += min(x-1,n-y)
     r += min(n-x,y-1)
     r += min(x-1,y-1)
     r += min(n-x,n-y)
     print(r)