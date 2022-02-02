def average(array):
    b=0
    list1=[]
    for i in array:
        if i not in list1:
            list1.append(i)
    for j in range(len(list1)):
        b+=list1[j]
    c=b/len(list1)
    return c
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)