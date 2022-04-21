for i in range(int(input())):
    a=int(input())
    str1=input()
    b=0
    for i in range(len(str1)):
        if str1[i]=="0":
            b+=1
    c=120-b
    if (c/120)>=0.75:
        print("YES")
    else:
        print("NO")