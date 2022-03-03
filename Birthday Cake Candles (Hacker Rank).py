a=int(input())
b=list(map(int, input().split()))
b.sort(reverse=True)
c=0
print(b)
for i in range(len(b)):
    if b[0]==b[i]:
        c+=1
print(c)