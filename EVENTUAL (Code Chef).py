# cook your dish here
for i in range(int(input())):
    a=int(input())
    b=input()
    c=0
    for i in b:
        if b.count(i)%2==0:
            c+=1
        else:
            print("NO")
            break
    if c==len(b):
        print("YES")
