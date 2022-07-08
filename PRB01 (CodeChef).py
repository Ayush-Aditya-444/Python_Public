for tc in range(int(input())):
    n=int(input())
    l=0
    for j in range(1,n+1):
        if n%j == 0:
            l+=1
    if l==2:
        print('yes')
    else:
        print('no')