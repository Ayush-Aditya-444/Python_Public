a, b, ar, br = 0, 0, 0, 0
for n in range(int(input())):
    p, q = map(int, input().split())
    a = a + p
    b = b + q
    ans = a - b
    if ans > 0 and ans > ar:
        ar = ans
        br = 1
    elif ans < 0 and abs(ans) > ar:
        ar = abs(ans)
        br = 2
print(br, ar)
