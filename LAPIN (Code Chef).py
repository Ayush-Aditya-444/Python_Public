for _ in range(int(input())):
    S = input()
    h = len(S)
    if h%2 == 0:
        s1 = S[0:h//2]
        s2 = S[h//2:]
    else:
        s1= S[0:h//2]
        s2 = S[(h+1)//2:]
    if sorted(s1) == sorted(s2):
        print('YES')
    else:
        print("NO")