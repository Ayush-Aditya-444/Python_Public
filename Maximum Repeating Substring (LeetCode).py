class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(sequence) < len(word):
            return 0
        count1=0
        count2=1
        while word*count2 in sequence:
            count1+=1
            count2+=1
        return count1