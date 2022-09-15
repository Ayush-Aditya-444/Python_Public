def ayush(list1):
    list1.sort(key=lambda x:x[1])
    count1=1
    start,end=list1[0]
    for i,j in list1:
        if i<=end:
            pass
        else:
            start=i
            end=j
            count1+=1
    return count1

list1=[[1,4],[2,3],[4,6],[8,9]]
print(ayush(list1))