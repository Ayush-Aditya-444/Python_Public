def ayush(list1):
    list2=sorted((x,i) for i,x in enumerate(list1))
    list3=[1]*len(list1)
    count1=0
    for _,i in list2:
        if i>0 and list1[i]>list1[i-1]:
            list3[i]=max(list3[i],list3[i-1]+1)
        if i<len(list1)-1 and list1[i]>list1[i+1]:
            list3[i]=max(list3[i],list3[i+1]+1)
    return sum(list3)
list1=[1,2,7,4,3,3,1]
print(ayush(list1))