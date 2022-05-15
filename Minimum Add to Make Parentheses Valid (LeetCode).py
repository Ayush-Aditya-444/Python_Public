class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if "(" == s[i]:
                stack.append(s[i])
            elif ")"==s[i]:
                if not stack or stack[-1]==")":
                    stack.append(")")
                else:
                    stack.pop()
        return len(stack)