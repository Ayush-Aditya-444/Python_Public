# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if c%a==0 and c%b==0:
        print("ANY")
    elif c%a==0:
        print("CHICKEN")
    elif c%b==0:
        print("DUCK")
    else:
        print("NONE")