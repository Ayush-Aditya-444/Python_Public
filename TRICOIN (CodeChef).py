for i in range(int(input())):
    a=int(input())
    b=0
    c=1
    while a>=c:
        a-=c
        b+=1
        c+=1
    print(b)    