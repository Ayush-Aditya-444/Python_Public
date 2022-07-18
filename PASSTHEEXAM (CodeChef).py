# cook your dish here
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a>=10 and b>=10 and c>=10 and a+b+c>=100:
        print("PASS")
    else:
        print("FAIL")