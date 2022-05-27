class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(a)):
            if a[i] not in sentence:
                return False
        return True