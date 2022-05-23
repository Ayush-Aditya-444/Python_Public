# cook your dish here
for i in range(int(input())):
    a=input()
    count1=0
    count2=0
    for i in range(len(a)):
        if a[i]=="0":
            count1+=1
        else:
            count2+=1
    if count1<count2:
        print("WIN")
    else:
        print("LOSE")