# cook your dish here
from  collections import Counter
for _ in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    count1=0
    dict1={}
    list2=[]
    for k in range(len(list1)):
        if k+1==list1[k]:
            list2.append(k+1)
        if list1[k] not in dict1:
            dict1[list1[k]]=1
        else:
            dict1[list1[k]]+=1
    for i,j in dict1.items():
        if j>=b and i not in list2:
            count1+=1
    print(count1)