def ayush(list1,list2):
    list1.sort()
    list2.sort()
    count1=0
    for i in range(len(list1)):
        if abs(list1[i]-list2[i])>count1:
            count1=abs(list1[i]-list2[i])
    return count1
list1=[3,2,-4]
list2=[0,-2,4]
print(ayush(list1,list2))