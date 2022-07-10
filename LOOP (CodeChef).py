t=int(input())
for i in range(t):
    a,b,m=map(int,input().split())
    if a>b:
        temp=a
        a=b
        b=temp
    def solve():
        ans1=b-a
        ans2=m-b+a
        return min(ans1,ans2)
    print(solve())
