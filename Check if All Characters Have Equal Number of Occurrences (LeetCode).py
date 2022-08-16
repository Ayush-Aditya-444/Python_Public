class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1=Counter(s)
        value1=dict1.values()
        max1=max(value1)
        min1=min(value1)
        if min1==max1:
            return True
        return False