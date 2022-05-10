a=input()
for i in range(int(input())):
    b=input()
    for i in b:
        if i not in a:
            print("No")
            break
        else:
            print("Yes")
