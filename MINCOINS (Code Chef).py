a=int(input())
for i in range(a):
    b=int(input())
    c=0
    if b%10==0 or b%5==0:
        while True:
            if b%10==0 and b>0:
                c=c+1
                b=b-10
            elif b%5==0 and b>0:
                c=c+1
                b=b-5
            else:
                break
        print(c)
    else:
        print(-1)