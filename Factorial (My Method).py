a=int(input())
for i in range(a):
    b=int(input())
    c=5
    j=1
    e=0
    while True:
        if(b>c**j):
            e+=(b//(c**j))
            j+=1
        else:
            break
    print(e)