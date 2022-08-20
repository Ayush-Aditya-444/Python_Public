class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1=Counter(s)
        count1=0
        count2=0
        for i,j in dict1.items():
            if j%2==0:
                count1+=j
            elif j%2!=0:
                count1+=j-1
                count2=1
        if count2==0:
            return count1
        else:
            return count1+1