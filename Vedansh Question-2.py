string = str(input())
stack = []
for i in range(len(string)):
    if string[i] in "([{":
        stack.append(string[i])
    else:
        if not stack:
            print("Invalid")
            break
        ch = stack.pop()
        if (ch == '(' and not string[i] == ')') or \
           (ch == '{' and not string[i] == '}') or \
           (ch == '[' and not string[i] == ']'):
            print("Invalid")
            break
else:
    if not stack:
        print("Valid")
    else:
        print("Invalid")