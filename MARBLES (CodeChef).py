try:
    for i in range(int(input())):
        n,k=map(int,input().split())
        count=1
        for i in range(1,k):
            count=count*(n-k+i)//i
        print(count)
except:
    pass