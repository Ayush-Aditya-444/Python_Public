def counts(teamA,teamB):
    list1=[]
    for i in range(len(teamB)):
        count1=0
        for j in range(len(teamA)):
            if teamB[i]>=teamA[j]:
                count1+=1
        list1.append(count1)
        count1=0
    return list1
teamA=[1,4,2,4]
teamB=[3,5]
a=counts(teamA,teamB)
print(a)