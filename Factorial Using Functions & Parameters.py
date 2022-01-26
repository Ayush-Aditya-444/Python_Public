def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    print("Calculation: ", end="")
    for i in range(n):
        print(f"{n} x", end=" ")
        n-=1
        if n==1:
            print(f"{1}")
            break
        else:
            continue
    return sum
while True:
    n=int(input("Enter Your Number:- "))
    print(f"Factorial Value: {factorial(n)}")