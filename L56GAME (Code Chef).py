for _ in range(int(input())):
    n=int(input())
    o=0
    e=0
    l=list(map(int,input().split()))
    for i in range(0,len(l)):
        if l[i]%2!=0:
            o=o+1
        else:
            e=e+1
    if o%2==0:
        print(1)
    elif o==1 and e==0:
        print(1)
    else:
        print(2)