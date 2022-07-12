# cook your dish here
for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    ans = 0
    for i in range(0,a):
        ans = max(ans, list1[i] + list1[i-1])
        
    print(ans)