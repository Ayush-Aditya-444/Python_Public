# cook your dish here
r1=int(input())
for i in range(r1):
    p1,q,s=map(str,input().split())
    x,y=map(str,input().split())
    if p1==x or p1==y:
        print(p1)
    elif q==x or q==y:
        print(q)
    else:
        print(s)