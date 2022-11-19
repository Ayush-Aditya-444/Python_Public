# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    int1=a*b
    if int1%4==0:
        print(int1//4)
    else:
        print(int1//4+1)