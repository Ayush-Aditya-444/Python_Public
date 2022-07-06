t=int(input())
for _ in range(t):
    a=input()
    a=list(a)
    c=0
    for i in range(0,len(a),2):
        if a[i]=='A' and a[i+1]=='B' or a[i]=='B' and a[i+1]=='A' :
            c=1 
        else:
            c=0
            break
    if c==1:
        print("yes")
    else:
        print("no")