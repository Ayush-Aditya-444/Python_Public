class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        if s.join(word1)==s.join(word2):
            return True
        else:
            return False