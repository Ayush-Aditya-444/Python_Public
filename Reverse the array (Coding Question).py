#Method 1 (Slicing) (Better)
def ayush1(list1):
    return list1[::-1]

#Method 2 (Stack)
def ayush2(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(list1[len(list1)-i-1])
    return list2

#Method 3 (Swapping)
def ayush3(list1):
    for i in range(len(list1)//2):
        list1[i],list1[len(list1)-i-1]=list1[len(list1)-1-i],list1[i]
    return list1

list1=list(map(int, input().split()))
print(ayush1(list1))
print(ayush2(list1))
print(ayush3(list1))