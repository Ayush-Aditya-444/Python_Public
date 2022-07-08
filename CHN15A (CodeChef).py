# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    count1=0
    for i in range(a):
        c=list1[i]+b
        if c%7==0:
            count1+=1
        else:
            continue
    print(count1)