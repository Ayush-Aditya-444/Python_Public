# cook your dish here
for i in range(int(input())):
    a=int(input())
    b=list(map(int, input().split()))
    count1=0
    for i in range(len(b)):
        if b[i]>=1000:
            count1+=1
    print(count1)