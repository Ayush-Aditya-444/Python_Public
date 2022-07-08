for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    a.reverse()
    high=len(a)
    for i in range(len(a)):
        if a[i]==0:
            high=high-1
        else:
            break
    print(high-1)