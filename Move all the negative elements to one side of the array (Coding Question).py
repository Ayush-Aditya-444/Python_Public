#Method-1 (Stack)
def ayush1(list1):
    list2=[]
    i=0
    while i!=len(list1)-1:
        if list1[i]<0:
            list2.append(list1[i])
            list1.pop(i)
        else:
            i+=1
    list2=list2+list1
    return list2

#Method-2 (Swapping)
def ayush2(list3):
    int1=0
    for i in range(len(list3)):
        if list3[i]<0:
            list3[i],list3[int1]=list3[int1],list3[i]
            int1+=1
    return list3

#Method-2 (Two Pointer) (Better)
def ayush3(list4):
    int1=len(list4)-1
    for i in range(len(list4)//2):

        if list4[i]<0 and list4[int1]<0:
            list4[i+1],list4[int1]=list4[int1],list4[i+1]

        elif list4[i]>0 and list4[int1]<0:
            list4[i],list4[int1]=list4[int1],list4[i]

        elif list4[i]>0 and list4[int1]>0:
            list4[i],list4[int1-1]=list4[int1-1],list4[i]

        int1-=1
    return list4

list1=list(map(int, input().split()))
list3=list1[:]
list4=list1[:]
print(ayush1(list1))
print(ayush2(list3))
print(ayush3(list3))