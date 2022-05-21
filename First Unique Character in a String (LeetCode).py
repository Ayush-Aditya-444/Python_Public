class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for i,j in enumerate(s):
            if c[j]<=1:
                return i
        return -1