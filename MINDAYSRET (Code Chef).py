# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a%b==0:
        print(a//b)
    else:
        print((a//b)+1)