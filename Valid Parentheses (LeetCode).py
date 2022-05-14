class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                    break
                ch = stack.pop()
                if (ch == '(' and not s[i] == ')') or \
                   (ch == '{' and not s[i] == '}') or \
                   (ch == '[' and not s[i] == ']'):
                    return False
                    break
        else:
            if not stack:
                return True
            else:
                return False