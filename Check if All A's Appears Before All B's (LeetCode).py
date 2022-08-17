class Solution:
    def checkString(self, s: str) -> bool:
        s=list(s)
        a=sorted(s)
        if a==s:
            return True
        else:
            return False