t=int(input())
x=y=k=0
l=[]
for i in range(t):
    a,b=map(int,input().split())
    x+=a
    y+=b
    z=x-y
    if z>0 and z>k:
        k=z
        p=1
    elif z<=0 and abs(z)>k:
        k=abs(z)
        p=2
print(p,k)