t =int(input())
for j in range(t):
    s = int(input())
    a = list(map(int,input().split()))
    for i in range(1,s):
        if a[i-1] > a[i]:
            a[i],a[i-1] = a[i-1],a[i]
            break
    if sorted(list(a)) == a:
        ans = 'YES'
    else:
        ans = 'NO'
    
    print(ans)