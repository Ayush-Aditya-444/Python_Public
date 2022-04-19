# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    list2=[]
    for i in range(a):
        if b-list1[i]>=0:
            b-=list1[i]
            list2.append("1")
        else:
            list2.append("0")
    print("".join(list2))
