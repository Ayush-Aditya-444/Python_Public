while(True):
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    a.insert(0,0)
    ia=[0]*(n+1)
    for i in range(n+1):
        ia[a[i]]=i
    if a==ia:
        print("ambiguous")
    else:
        print("not ambiguous")