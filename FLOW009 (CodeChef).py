t = int(input())
for i in range(t):
    q,p = map(int,input().split())
    a = q*p
    b = 0.1*a
    if(q>1000):
        print(a-b)
    else:
        print(a)