for i in range(int(input())):
    length_list1=int(input())
    list1=list(map(int, input().split()))
    count1=0
    list2=[]
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            if list1[i]<list1[j]:
                count1+=1
        list2.append(count1)
        count1=0
    print(*list2)
        