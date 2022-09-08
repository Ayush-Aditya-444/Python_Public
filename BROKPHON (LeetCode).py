# cook your dish here
for _ in range(int(input())):
    int1=int(input())
    list1=list(map(int, input().split()))
    list2=[]
    for i in range(len(list1)-1):
        if list1[i]!=list1[i+1]:
            list2.append(i)
            list2.append(i+1)
    print(len(set(list2)))
            
            