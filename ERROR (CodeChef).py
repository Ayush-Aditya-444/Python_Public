for i in range(int(input())):
    a=input()
    for i in range(len(a)-2):
        if a[i]=="0" and a[i+1]=="1" and a[i+2]=="0":
            print("Good")
            break
        elif a[i]=="1" and a[i+1]=="0" and a[i+2]=="1":
            print("Good")
            break
        else:
            print("Bad")