#Method-1 (Iterative)
def ayush1(list1):
    list2=[]
    for i in range(len(list1)):
        int1=(i-1)%len(list1)
        list2.append(list1[int1])
    return list2

#Method-2 (Swapping) (Better)
def ayush2(list1):
    temp=list1[0]
    for i in range(len(list1)):
        temp,list1[(i+1)%len(list1)]=list1[(i+1)%len(list1)],temp
    return list1

list1=list(map(int, input().split()))
print(ayush1(list1))
print(ayush2(list1))