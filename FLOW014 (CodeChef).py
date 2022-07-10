t = int(input())
for i in range(t):
    h,c,t = map(float,input().split())
    h1 = h > 50
    c1 = c < 0.7
    t1 = t > 5600
    if h1 and c1 and t1:
        print(10)
    elif h1 and c1:
        print(9)
    elif c1 and t1:
        print(8)
    elif h1 and t1:
        print(7)
    elif h1 or c1 or t1:
        print(6)
    else:
        print(5)