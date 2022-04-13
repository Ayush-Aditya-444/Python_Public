for i in range(int(input())):
    a,b,c=map(int, input().split())
    d,e,f=map(int, input().split())
    g=0
    if a>d:
        g+=1
    else:
        g-=1
    if b>e:
        g+=1
    else:
        g-=1
    if c>f:
        g+=1
    else:
        g-=1
    if g>0:
        print("A")
    else:
        print("B")