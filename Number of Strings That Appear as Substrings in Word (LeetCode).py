class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count1=0
        for i in range(len(patterns)):
            if patterns[i] in word:
                count1+=1
        return count1