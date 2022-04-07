for i in range(int(input())):
    a,b=map(int, input().split())
    c=0
    for j in range(a,b+1):
        if j%10==2 or j%10==3 or j%10==9:
            a+=1
        else:
            continue
    print(c)