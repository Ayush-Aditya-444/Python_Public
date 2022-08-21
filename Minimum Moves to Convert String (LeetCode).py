class Solution:
    def minimumMoves(self, s: str) -> int:
        s=list(s)
        i=0
        count1=0
        while i<len(s):
            if s[i]=="X":
                count1+=1
                i+=3
            else:
                i+=1
        return count1