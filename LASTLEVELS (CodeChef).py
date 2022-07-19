# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a<=3:
        print(a*b)
    else:
        if a%3!=0:
            z=a//3
            print((b*a)+(z*c))
        else:
            z=(a//3)-1
            print((b*a)+((z)*c))