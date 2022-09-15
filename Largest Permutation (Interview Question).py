def ayush(list1,swap):
    i=0
    max=len(list1)
    dict1={x:i for i,x in enumerate(list1)}
    while swap!=0 and i!=len(list1):
        int1=dict1[max]
        if i==dict1[max]:
            pass
        else:
            list1[i],list1[int1]=list1[int1],list1[i]
            dict1[list1[i]],dict1[list1[int1]]=dict1[list1[int1]],dict1[list1[i]]
            swap-=1
        i+=1
        max-=1
    return list1

list1=[3,2,4,1,5]
swap=3
print(ayush(list1,swap))