# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    lifetime = list(map(int,input().split()))
    
    if((n*x - sum(lifetime))<0):
        print(0)
    else:
        print(n*x - sum(lifetime))