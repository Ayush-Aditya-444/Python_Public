for i in range(int(input())):
    x=int(input())
    list1=list(map(int, input().split()))
    count=0
    for i in list1:
        if i>=10 and i<=60:
            count+=1
    print(count)