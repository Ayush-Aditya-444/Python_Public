for _ in range(int(input())):
    length_str,X,Y=map(int, input().split())
    str1=input()
    list1=[]
    for i in range(len(str1)):
        list1.append(int(str1[i]))
    num1=num2=0
    if X>Y:
        list1.sort(reverse=True)
        for j in range(len(list1)-1):
            if list1[j]==0 and list1[j+1]==1:
                num1+=1
            elif list1[j]==1 and list1[j+1]==0:
                num2+=1
        print((X*num1)+(Y*num2))
    else:
        list1.sort()
        for k in range(len(list1)-1):
            if list1[k]==0 and list1[k+1]==1:
                num1+=1
            elif list1[k]==1 and list1[k+1]==0:
                num2+=1
        print((X*num1)+(Y*num2))