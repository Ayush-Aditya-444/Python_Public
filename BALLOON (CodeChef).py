# cook your dish here
for _ in range(int(input())):
    list1=[1,2,3,4,5,6,7]
    a=int(input())
    list2=list(map(int, input().split()))
    count1=0
    for i in list2:
        if len(list1)==0:
            break
        elif i in list1:
            list1.remove(i)
        count1+=1
    print(count1)