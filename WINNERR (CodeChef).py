# cook your dish here
t=int(input())
for i in range(t):
    p1,p2,q1,q2=map(int,input().split())
    if(max(p1,p2)<max(q1,q2)):
        print("p")
    elif(max(p1,p2)>max(q1,q2)):
        print("q")
    else:
        print("tie")