n = int(input())
a=[]
for i in range(1,n+1):
    if  i not in a:
        a.append(i)
for j in a:  
    print(j, end = "")  