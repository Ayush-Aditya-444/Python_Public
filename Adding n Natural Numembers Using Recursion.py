def ayush(n):
    if n==1:
        return n
    else:
        return n+ayush(n-1)
n=5
a=ayush(n)
print(a)