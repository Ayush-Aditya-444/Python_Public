class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        for i in range(len(t)):
            if t[i] not in s:
                return t[i]
            elif t[i] in s:
                if t.count(t[i])!=s.count(t[i]):
                    return t[i]
            