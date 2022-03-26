# cook your dish here
n = int(input())
for i in range(n):
    n1,n2 = map(int,input().split(' '))
    if abs(n1-n2)==1:
        if min(n1,n2)%2==0:
            print('NO')
        else:
            print('YES')
    elif abs(n1-n2)==2:
        if n1%2==0 and n2%2==0:
            print('YES')
        else:
            print('YES')
    else:
        print('NO')