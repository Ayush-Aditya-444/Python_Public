t=int(input())
for i in range(t):
    d,x,y,z=map(int,input().split())
    m=7*x
    n=y*d+(7-d)*z
    print(max(m,n))