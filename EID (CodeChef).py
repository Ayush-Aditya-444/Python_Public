# cook your dish here
for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list1.sort()
    b=list1[1]-list1[0]
    for i in range(1,len(list1)-1):
        c=list1[i+1]-list1[i]
        if b>c:
            b=c
    print(b)