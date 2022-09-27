# cook your dish here
a=int(input())
count1=0
for i in range(1,a//2+1):
    int1=a-i
    if int1==i:
        count1+=1
    else:
        count1+=2
print(count1)
