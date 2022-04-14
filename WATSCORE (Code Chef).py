for i in range (int(input())):
    N=(int(input()))
    ans=[0]*9
    for j in range (N):
        pi,si=map(int,input().split())
        if (pi>=1 and pi<=8 and si>ans[pi]):
            ans[pi]=si
    print(sum(ans))