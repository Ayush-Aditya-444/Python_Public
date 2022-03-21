number_of_input=int(input())
list1=[]
for i in range(number_of_input):
    list2=list(map(int, input().split()))
    a=(list2[0]*list2[1]//100)
    list1.append(a)
    continue
print(*list1)