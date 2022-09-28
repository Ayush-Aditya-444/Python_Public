#Method 1 (Iterative)
def ayush1(list1):
    max1=0
    min1=99999999999
    for i in range(len(list1)):
        if list1[i]>max1:
            max1=list1[i]
        if list1[i]<min1:
            min1=list1[i]
    return max1,min1

#Method 2 (Sorting) (Better)
def ayush2(list1):
    list1.sort()
    return list1[-1],list1[0]

list1=list(map(int, input().split()))
print(ayush1(list1))
print(ayush2(list1))
