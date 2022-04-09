# cook your dish here
t = int(input())
while(t):
    t-=1 
    h,x,y,c = map(int,input().split())
    if h*(x + y//2) <= c:
        print("yes")
    else:
        print("no")