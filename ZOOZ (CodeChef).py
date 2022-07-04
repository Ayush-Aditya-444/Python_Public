testcases = int(input())

for i in range(testcases):
    n = int(input())
    if(n >= 4):
        s = '10' + '0' * (n-4) + '01'
    else:
        s = '101'
    print(s)