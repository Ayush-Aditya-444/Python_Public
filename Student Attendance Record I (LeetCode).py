class Solution:
    def checkRecord(self, s: str) -> bool:
        dict1=Counter(s)
        if dict1["A"]>=2:
            return False
        if "LLL" in s:
            return False
        return True