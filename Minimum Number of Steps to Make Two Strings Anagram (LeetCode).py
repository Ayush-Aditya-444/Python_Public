class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1=Counter(s)
        t=Counter(t)
        dict1=dict1 & t
        sum1=sum(dict1.values())
        return len(s)-sum1