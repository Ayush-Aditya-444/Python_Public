# cook your dish here
a=int(input())
list1=list(map(int, input().split()))
count1=0
count2=0
for i in range(a):
    if list1[i]%2==0:
        count1+=1
    else:
        count2+=1
if count1>count2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")