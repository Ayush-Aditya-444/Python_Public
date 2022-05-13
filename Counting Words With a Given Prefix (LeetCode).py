class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count1=0
        for word in words:
            if pref in word[:len(pref)]:
                count1+=1
        return count1