# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int, input().split())
    int1=c//b
    int2=c%b
    if(b*a>c):
        print((int1)*(b**2)+int2**2)
    else:
        print(a*b**2)