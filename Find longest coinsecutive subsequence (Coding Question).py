def ayush(arr):
#code here
    set1=set(arr)
    int1=min(set1)
    count1=0
    count2=0
    i=0
    while len(set1)!=0:
        if int1 in set1:
            set1.remove(int1)
            int1+=1
            count1+=1
        else:
            if count1>count2:
                count2=count1
            int1=min(set1)
            count1=0
    if count1>count2:
        return count1
    return count2
arr=[2,6,1,9,4,5,3]
print(ayush(arr))