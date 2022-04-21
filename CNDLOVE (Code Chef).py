for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    if sum(list1)%2==0:
        print("NO")
    else:
        print("YES")