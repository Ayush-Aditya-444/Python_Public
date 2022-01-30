a=list(map(int, input().split()))
b=a[0]-a[1]
if (b%5==4):
    print(b-1)
elif b%5==1:
    print(b+1)
else:
    print(b+1)