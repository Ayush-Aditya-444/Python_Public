def ayush(n):
    if n<=1:
        return n
    return ayush(n-1)+ayush(n-2)
n=10
a=ayush(n)
print(a)