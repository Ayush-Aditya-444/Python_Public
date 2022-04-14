for i in range(int(input())):
    n=int(input())
    first=[]
    last=[]
    for i in range(n):
        a,b=map(str,input().split())
        first.append(a)
        last.append(b)
    for i in range(n):
        if (first.count(first[i])>1):
            print(first[i],end=" ")
            print(last[i])
        else:
            print(first[i])