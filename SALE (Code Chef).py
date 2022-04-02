for _ in range(int(input())):
        A=list(map(int,input().split()))
        s=sum(A)-min(A)
        print(s)