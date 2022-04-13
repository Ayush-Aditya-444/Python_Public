for i in range(int(input())):
    a=input()
    b=0
    for i in range(len(a)):
        if a[i]=="1":
            b+=1
    if b==0:
        print("Beginner")
    elif b==1:
        print("Junior Developer")
    elif b==2:
        print("Middle Developer")
    elif b==3:
        print("Senior Developer")
    elif b==4:
        print("Hacker")    
    else:
        print("Jeff Dean")
        