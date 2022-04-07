for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=b=c=0
    j=0
    k=1
    for i in range(len(list1)//2):
        a=a+list1[j]
        j=j+2
    for c in range(len(list1)//2):
        b=b+list1[k]
        k=k+2
    if a==b:
        print(0)
    elif a>b:
        print(1)
    else:
        print(2)