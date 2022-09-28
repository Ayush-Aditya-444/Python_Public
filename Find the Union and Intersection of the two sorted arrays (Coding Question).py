#Method-1 (Hashset) (Better)
def ayush1(list1,list2):
    set1=set(list1)
    set2=set(list2)
    set3=set1.union(set2)
    set4=set1.intersection(set2)
    return list(set3),list(set4)

#Method-2 Iterative
def ayush2(list1,list2):
    int1=len(list1)
    int2=len(list2)
    list3=[]
    if int1>int2:
        for i in range(len(list2)):
            if list2[i] in list1:
                list3.append(list2[i])
                p=0       
        for i in range(len(list2)):
            if list2[i] not in list1:
                list1.append(list2[i])
                p=0
    else:
        for i in range(len(list1)):
            if list1[i] in list2:
                list3.append(list1[i])
                p=1
        for i in range(len(list1)):
            if list1[i] not in list2:
                list2.append(list1[i])
                p=1
    if p==0:
        return list1,list3
    else:
        return list2,list3

list1=list(map(int, input().split()))
list2=list(map(int, input().split()))

print(ayush1(list1,list2))
print(ayush2(list1,list2))