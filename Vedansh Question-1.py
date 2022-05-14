string = str(input())
stack = []
for i in range(len(string)):
    if "(" == string[i]:
        stack.append(string[i])
    else:
        if not stack:
            print("Invalid")
            break
        stack.pop()
else:
    if not stack:
        print("Valid")
    else:
        print("Invalid")