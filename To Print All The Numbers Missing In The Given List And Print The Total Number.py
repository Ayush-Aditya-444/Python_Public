print("List 1:-")
list1=[]
for i in range(1,101):
    list1.append(i)
print(list1)
print("List 2:-")
list2=[1,4,5,77,88,43,5,67,82,100]
for i in range(1,101):
    if i not in list2:
        list2.append(i)
        print(i)
list2.sort()
print(list2)
