# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,n-1):
        if a[i] == a[i+1]:
            c+=1
    print(len(a)-c)
