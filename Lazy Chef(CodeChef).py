print("Enter No. Of Test Cases:-")
for i in range(int(input())):
    b=input().split()
    c=int(b[0])
    d=int(b[1])
    e=int(b[2])
    f=c*d
    g=c+e
    if f>g:
        print(f("Time Taken {g}sec."))
    else:
        print(f)