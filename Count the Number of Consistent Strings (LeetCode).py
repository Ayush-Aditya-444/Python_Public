class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(list(allowed))
        ans=0
        for i in words:
            t=set(list(i))
            if t.issubset(a):
                ans+=1
        return ans