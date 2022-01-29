a=int(input())
for i in range(a):
    b=list(map(int, input().split()))
    b.sort()
    c=[]
    for i in range(0,len(b)-1):
        d=b[i]-b[i+1]
        c.append((-1)*d)
    c.sort()
    print(c[0])