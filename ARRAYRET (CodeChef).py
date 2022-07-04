# cook your dish here
for i in range(int(input())):
    n=int(input())
    B=[int(k) for k in input().split()]
    b=sum(B)//(n+1)
    A=[]
    for k in range(n):
        A.append(B[k]-b)
    print(*A) 