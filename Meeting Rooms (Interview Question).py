def ayush(list1):
    list2=[]
    for i,j in list1:
        list2.append((i,1))
        list2.append((j,-1))
    list2.sort()
    count1=0
    max1=0
    for i,j in list2:
        count1+=j
        max1=max(max1,count1)
    return max1
list1=[[5,10],[15,20],[0,30]]
print(ayush(list1))