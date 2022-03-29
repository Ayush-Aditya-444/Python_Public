a=int(input())
list1=[]
for i in range(1,11):
    if a%i==0:
        list1.append(i)
print(max(list1))