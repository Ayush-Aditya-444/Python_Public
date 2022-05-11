class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r=0
        count_l=0
        count_out=0
        for i in range(len(s)):
            if s[i]=="R":
                count_r+=1
            else:
                count_l+=1
            if count_r==count_l:
                count_out+=1
        return count_out