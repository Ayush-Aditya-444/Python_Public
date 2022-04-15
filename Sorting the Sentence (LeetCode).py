class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = {}
        for i in a :
            b[i[-1]] = i[:-1]
        return ' '.join([b[j] for j in sorted(b)])