# cook your dish here
for i in range(int(input())):
    a=input()
    a=list(a)
    count1=0
    for i in range(len(a)):
        if a[i]=="4":
            count1+=1
    print(count1)    