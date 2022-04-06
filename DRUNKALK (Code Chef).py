# cook your dish here
for i in range(int(input())):
        a=int(input())
        b=0
        for i in range(1,a+1):
            if i%2==1:
                b=b+3
            else:
                b=b-1
        print(b)
