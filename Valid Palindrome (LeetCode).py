class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.upper()
        stack=[]
        for i in range(len(s)):
            if ord(s[i])>=65 and ord(s[i])<=90:
                stack.append(s[i])
            elif ord(s[i])>=48 and ord(s[i])<=57:
                stack.append(s[i])
        a=stack[::-1]
        if stack==a:
            return True
        else:
            return False