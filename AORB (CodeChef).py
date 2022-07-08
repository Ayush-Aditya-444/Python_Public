# cook your dish here
for i in range(int(input())):
    p,q=map(int,input().split())
    a=(500-(p*2))+(1000-((q+p)*4))
    b=(1000-q*4)+(500-(p+q)*2)
    print(max(a,b))