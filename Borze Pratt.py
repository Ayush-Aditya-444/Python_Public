s = input()
num = ''
i = 0
n = True
while n:
    try:
        if s[i] == '-' and s[i + 1] == '.':
            num += '1'
            i += 2
            continue
        if s[i] == '-' and s[i + 1] == '-':
            num += '2'
            i += 2
            continue
        elif s[i] == '.':
            num += '0'
            i += 1
            continue
    except IndexError:
        break
print(num)
