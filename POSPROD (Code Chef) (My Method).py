# cook your dish here
for i in range(int(input())):
    a=int(input())
    b=0
    list1=list(map(int, input().split()))
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i]*list1[j]>0 and i<j:
                b+=1
    print(b)