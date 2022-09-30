def ayush(list1,k):
    list1.sort()
    int1=list1[-1]-list1[0]
    for i in range(1,len(list1)):
        if list1[i]<k:
            continue
        min1=min(list1[0]+k,list1[i]-k)
        max1=max(list1[-1]-k,list1[i-1]+k)
        int1=min(int1, max1-min1)
    return int1
list1=list(map(int, input().split()))
k=int(input())
print(ayush(list1,k))