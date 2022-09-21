# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    sum1=0
    for j in range(len(list1)):
        int1=abs(list1[j]-b)
        int2=abs(list1[j]-1)
        if int1>=int2:
            sum1+=int1
        else:
            sum1+=int2
    print(sum1)