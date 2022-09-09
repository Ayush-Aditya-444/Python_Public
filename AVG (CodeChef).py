# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    list1=list(map(int, input().split()))
    sum1=sum(list1)
    sum2=(a+b)*c
    sum3=(sum2-sum1)//b
    if sum2>sum1 and (sum2-sum1)%b==0:
        print(sum3)
    else:
        print(-1)