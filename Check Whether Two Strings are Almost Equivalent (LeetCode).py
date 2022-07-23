class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1=list(word1)
        word2=list(word2)
        set1=list(set(word1))
        set2=list(set(word2))
        for i in range(len(set1)):
            if abs(word1.count(set1[i])-word2.count(set1[i]))>3:
                return False
        for i in range(len(set2)):
            if abs(word2.count(set2[i])-word1.count(set2[i]))>3:
                return False
        return True