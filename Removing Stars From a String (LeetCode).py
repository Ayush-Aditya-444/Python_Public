class Solution:
    def removeStars(self, s: str) -> str:
        str1=[]
        for i in range(len(s)):
            if s[i]=="*":
                str1.pop()
            else:
                str1.append(s[i])
        return "".join(str1)