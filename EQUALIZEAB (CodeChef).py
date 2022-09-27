# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int, input().split())
    int1=abs(a-b)/2
    if int1%c==0:
        print("YES")
    else:
        print("NO")
        
            