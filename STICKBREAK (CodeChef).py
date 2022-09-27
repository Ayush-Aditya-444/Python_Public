# cook your dish here
for _ in range(int(input())):
    a,b=map(int, input().split())
    if a%b==0:
        print(a%b)
    else:
        print(1)