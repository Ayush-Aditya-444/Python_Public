from collections import Counter

#Method-1
def ayush1(list1):
    dict1=Counter(list1)
    list2=([0]*dict1[0])+([1]*dict1[1])+([2]*dict1[2])
    return list2

#Method-2 (Better)
def ayush2(list1):
        int0=0
        int1=0
        int2=0
        for i in range(len(list1)):
            if list1[i]==0:
                int0+=1
            elif list1[i]==1:
                int1+=1
            else:
                int2+=1
        for i in range(len(list1)):
            if int0!=0:
                list1[i]=0
                int0-=1
            elif int1!=0:
                list1[i]=1
                int1-=1
            elif int2!=0:
                list1[i]=2
                int2-=1
        return list1


list1=list(map(int, input().split()))
print(ayush1(list1))
print(ayush2(list1))