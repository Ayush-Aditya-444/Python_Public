print("Enter No. Of Test Cases:-")
for i in range(int(input())):
    a=input().split()
    b=int(a[0])
    c=int(a[1])
    d=int(a[2])
    e=int(a[3])
    if b+d==180 and c+e==180:
        print("YES")
    else:
        print("NO")