class Solution:
    def replaceDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            try:
                stack.append(s[i])
                if stack[-1].isnumeric():
                    b=ord(stack[-2])+int(stack[-1])
                    stack.append(chr(b))
                    stack.pop(-2)
            except IndexError:
                continue
        return "".join(stack)