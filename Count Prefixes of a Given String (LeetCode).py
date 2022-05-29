class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count1=0
        for i in words:
            if (s[:len(i)]==i):
                count1+=1
        return count1