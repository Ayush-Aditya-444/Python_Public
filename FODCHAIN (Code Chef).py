for i in range(int(input())):
    a,b=map(int, input().split())
    c=0
    while a//b>0:
       a=a//b
       c=c+1
    print(c+1) 