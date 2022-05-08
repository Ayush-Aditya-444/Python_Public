# cook your dish here
# cook your dish here
t=int(input())
for tc in range(t):
    n=int(input())
    ml=[]
    for i in range(n):
        l1=list(map(int,input().split()))
        ml.append(l1)
    res=0
    t=0
    for i in range(n):
        x=i
        y=0
        t=0
        while x<n:
            t=t+ml[x][y]
            x=x+1 
            y=y+1
        res=max(res,t)
        y=i 
        x=0
        t=0
        while y<n:
            t=t+ml[x][y]
            x=x+1 
            y=y+1
        res=max(res,t)
    print(res)
    
    
        
