def ayush(n,sum1):
    if n<=1:
        return sum1
    sum1=sum1*(n)
    return ayush(n-1,sum1)
n=5
sum1=1
a=ayush(n,sum1)
print(a)