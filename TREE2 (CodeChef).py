for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    temp=-1
    l.sort()
    count=0
    for i in range(n):
        if l[i]!=0 and l[i]!=temp:
            count+=1
            temp=l[i]
    print(count)