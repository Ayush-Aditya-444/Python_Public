key = {0:0, 1:1, 2:2, 3:3, 4:4}

def solve(n):
    if n in key:
        return key[n]
    else:
        key[n] = max(n,solve(n//2) + solve(n//3) + solve(n//4))
        return key[n]
    
while (1):
    try:
        n = int(input())
        print(solve(n))
    except:
        break