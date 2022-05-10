# cook your dish here
k,n = map(int,input().split())
a,b=[],[]
for i in range (k):
    a.append(input())
for j in range (n):
    b.append(input())
for x in b:
    if(len(x)>=47):
        print("Good")
    else:
        for y in a:
            if y in x:
                print("Good")
                break
        else:
            print("Bad")