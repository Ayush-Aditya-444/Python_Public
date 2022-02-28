a=int(input())
b=list(map(int, input().split()))
j=len(list(b))-1
for i in range(len(list(b))):
    print(b[j], end =" ")
    j-=1