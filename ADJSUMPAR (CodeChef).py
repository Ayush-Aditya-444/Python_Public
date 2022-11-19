# cook your dish here
for _ in range(int(input())):
    int1=int(input())
    list1=list(map(int, input().split()))
    if ( sum(list1)%2 == 0 ):
        print("YES")
    else:
        print("NO")
    
    