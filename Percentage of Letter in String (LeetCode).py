class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        s=list(s)
        int1=s.count(letter)
        return (int1*100)//len(s)