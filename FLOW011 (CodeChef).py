T=int(input())
for t in range(T):
    sal=float(input())
    if(sal<1500):
        sal=sal+sal*0.1+sal*0.9
        print(sal)
    else:
        sal=sal+500+sal*0.98
        print(sal)