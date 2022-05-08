for _ in range(int(input())):
    a,b=map(int, input().split())
    str1=input()
    list1=[b]
    for i in range(len(str1)):
        if str1[i]=="R":
            b+=1
            list1.append(b)
        else:
            b-=1
            list1.append(b)
    print(max(list1)-min(list1)+1)