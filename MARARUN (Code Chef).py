# cook your dish here
t = int(input())
for _ in range(t):
    D, d, A, B, C = list(map(int, input().split()))
    total_dist = D*d 
    if(total_dist < 10):
        print(0)
    elif(total_dist >= 10 and total_dist < 21):
        print(A)
    elif(total_dist >= 21 and total_dist < 42):
        print(B)
    else:
        print(C)