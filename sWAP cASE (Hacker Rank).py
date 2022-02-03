def swap_case(s):
    a=""
    for i in range(len(s)):
        if s[i].isupper():
            a+=s[i].lower()
        elif s[i].islower():
            a+=s[i].upper()
        else:
            a+=s[i]
    return a
s = input()
result = swap_case(s)
print(result)