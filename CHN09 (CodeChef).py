for i in range(int(input())):
    a=input()
    a=list(a)
    count1=0
    count2=0
    for i in range(len(a)):
        if a[i]=="a":
            count1+=1
        else:
            count2+=1
    print(min(count1,count2))