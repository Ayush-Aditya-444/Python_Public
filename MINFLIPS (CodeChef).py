t=int(input())
for op in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=abs(sum(a))
    if(s%2==0):
        print(s//2)
    else:
        print(-1)