for i in range(int(input())):
    a,b=map(int, input().split())    
    list1=list(map(int, input().split()))
    c=0
    for i in range(len(list1)):
        if list1[i]>b:
            c=c+b
        else:
            c=c+list1[i]
    print(sum(list1)-c)
