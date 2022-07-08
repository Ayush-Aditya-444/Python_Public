for i in range(int(input())):
    a=int(input())
    b=input()
    b=b.split()
    num1=0
    num2=0
    for i in range(len(b)):
        if b[i]=="START38":
            num1+=1
        else:
            num2+=1
    print(num1,num2)