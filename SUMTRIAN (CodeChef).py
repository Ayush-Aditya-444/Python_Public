# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    for _ in range(n):
        r=list(map(int,input().split()))
        l.append(r)
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            l[i][j]+=max(l[i+1][j], l[i+1][j+1])
    print(l[0][0])