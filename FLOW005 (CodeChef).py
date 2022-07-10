# cook your dish here
for i in range(int(input())):
    a=int(input())
    count1=0
    while a!=0:
        if a>=100:
            a-=100
            count1+=1
        elif a>=50:
            a-=50
            count1+=1
        elif a>=10:
            a-=10
            count1+=1
        elif a>=5:
            a-=5
            count1+=1
        elif a>=2:
            a-=2
            count1+=1
        elif a>=1:
            a-=1
            count1+=1
    print(count1)