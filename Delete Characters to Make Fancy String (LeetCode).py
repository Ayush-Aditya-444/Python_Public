class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        s=list(s)
        str1=s[0]+s[1]
        for i in range(2,len(s)):
            if s[i]!=str1[-1] or s[i]!=str1[-2]:
                str1+=s[i]
        return str1
    