# cook your dish here
for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list1.sort()
    list2=[]
    b=0
    c=-1
    for i in range(len(list1)):
        if i%2==0:
            list2.append(list1[b])
            b+=1
        elif i%2!=0:
            list2.append(list1[c])
            c=c-1
    print(*list2)