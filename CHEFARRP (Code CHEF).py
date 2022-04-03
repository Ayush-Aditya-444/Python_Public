# cook your dish here
for _ in range(int(input())):
    k=int(input())
    A=list(map(int,input().split()))
    new=[]
    c=0
    for i in range(len(A)+1):
        for j in range(i+1,len(A)+1):
            new.append(A[i:j])
            
    for x in new:
        q=0
        t=1
        for y in x:
            q+=y
            t*=y
        if(q==t):
            c+=1
    print(c)
