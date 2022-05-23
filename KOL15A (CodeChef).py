# cook your dish here
for i in range(int(input())):
    a=input()
    a=list(a)
    sum=0
    for i in range(len(a)):
        try:
            a[i]=int(a[i])
            sum+=a[i]
        except ValueError:
            continue
    print(sum)