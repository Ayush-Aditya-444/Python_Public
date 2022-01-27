print("Calculate Average In A given Lists:-")
list1=list(map(int,input().split()))
sum=0
for i in range(len(list1)):
    sum+=list1[i]
sum/=len(list1)
print(f"Average= {sum}")