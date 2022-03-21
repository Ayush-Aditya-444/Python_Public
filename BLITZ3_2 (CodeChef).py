number_of_input=int(input())
list1=[]
for i in range(number_of_input):
    list2=list(map(int, input().split()))
    a=(2*(180+list2[0]))-(list2[1]+list2[2])
    list1.append(a)
    continue
for i in range(len(list1)):
    print(list1[i])